import pandas as pd                                  # 데이터 처리를 위한 pandas 임포트

def load_epex_data(file_path):                       # 데이터 로드 함수 정의
    try:
        df = pd.read_csv(file_path)                  # CSV 파일 읽기
        df['timestamp'] = pd.to_datetime(df['timestamp']) # 문자열을 날짜 형식으로 변환
        df.set_index('timestamp', inplace=True)      # 시간을 인덱스로 설정 (시계열 필수)
        
        print("Successfully loaded data:")           # 성공 메시지 출력
        print(df.head())                             # 데이터 앞부분 확인
        return df                                    # 처리된 데이터프레임 반환
        
    except FileNotFoundError:                        # 파일이 없을 경우 예외 처리
        print("Error: File not found!")              # 에러 메시지
        return None                                  # None 반환

if __name__ == "__main__":                           # 스크립트 실행 시작점
    path = "sample_prices.csv"                       # 불러올 파일 경로
    epex_data = load_epex_data(path)                 # 함수 호출
    
    if epex_data is not None:                        # 데이터가 잘 로드되었다면
        print("\n--- Index Information ---")         # 구분선 출력
        print(epex_data.index)                       # 인덱스 전체 정보 출력
        print(f"Index DataType: {epex_data.index.dtype}") # 인덱스의 데이터 타입 출력