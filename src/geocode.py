"""선택 실행용 카카오 지오코딩. KAKAO_REST_API_KEY 환경변수 필요.
자동 분석 실행 중에는 외부 API를 호출하지 않는다. 실행 시 실패/미매칭도 저장한다.
"""
from src.paths import ROOT, data_path, result_path
import argparse,json,os,time
from pathlib import Path
import requests
import pandas as pd


def geocode_table(input_path,output_path,address_column,encoding='utf-8-sig',pause=0.15):
    key=os.environ.get('KAKAO_REST_API_KEY')
    if not key:raise ValueError('KAKAO_REST_API_KEY 환경변수를 설정하세요.')
    df=pd.read_csv(input_path,encoding=encoding)
    if address_column not in df:raise ValueError(f'주소 컬럼 없음: {address_column}')
    out=Path(output_path);out.parent.mkdir(parents=True,exist_ok=True)
    cache_path=out.with_suffix('.cache.json')
    cache=json.loads(cache_path.read_text()) if cache_path.exists() else {}
    headers={'Authorization':f'KakaoAK {key}'}
    rows=[]
    try:
        for value in df[address_column]:
            query='' if pd.isna(value) else str(value).strip()
            if query in cache:
                rows.append(cache[query]);continue
            row={'Longitude':None,'Latitude':None,'ADDRESS':None,'CODE':None,'geocode_status':'unmatched'}
            if query:
                try:
                    r=requests.get('https://dapi.kakao.com/v2/local/search/address.json',
                                   params={'query':query},headers=headers,timeout=20)
                    r.raise_for_status();docs=r.json().get('documents',[])
                    if docs:
                        doc=docs[0];x,y=float(doc['x']),float(doc['y'])
                        r=requests.get('https://dapi.kakao.com/v2/local/geo/coord2regioncode.json',
                                       params={'x':x,'y':y},headers=headers,timeout=20)
                        r.raise_for_status()
                        # 법정동(B)과 행정동(H)을 구분해서 H만 사용
                        h=next((d for d in r.json().get('documents',[]) if d.get('region_type')=='H'),None)
                        row.update(Longitude=x,Latitude=y)
                        if h:row.update(ADDRESS=h['region_3depth_name'],CODE=h['code'],geocode_status='ok')
                        else:row['geocode_status']='no_administrative_dong'
                except (requests.RequestException,ValueError,KeyError):
                    row['geocode_status']='request_or_response_error'
            rows.append(row)
            # 일시적 API 오류는 캐시하지 않아 재실행으로 재시도 가능
            if row['geocode_status']!='request_or_response_error':cache[query]=row
            time.sleep(pause)
    finally:
        cache_path.write_text(json.dumps(cache,ensure_ascii=False,indent=2),encoding='utf-8')
        if rows:
            result=df.iloc[:len(rows)].drop(columns=['Longitude','Latitude','ADDRESS','CODE','geocode_status'],errors='ignore')
            pd.concat([result.reset_index(drop=True),pd.DataFrame(rows)],axis=1).to_csv(out,index=False,encoding='utf-8-sig')
    return out


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--address-column',required=True)
    p.add_argument('--encoding',default='utf-8-sig');args=p.parse_args()
    print(geocode_table(args.input,args.output,args.address_column,args.encoding))
