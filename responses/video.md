# Video info

## list

### contentDetails
동영상의 길이, 동영상에 자막을 사용할 수 있는지 여부
```json
{
    "kind": "youtube#videoListResponse",
    "etag": "0tkY9icMP2jCOjsDvf0TnKW_cbY",
    "items": [
        {
            "kind": "youtube#video",
            "etag": "yF0mC6wC-rJkJI6Y8LIswZA7YUo",
            "id": "rWULE8_Dyt8",
            "contentDetails": {
                "duration": "PT2M55S",
                "dimension": "2d",
                "definition": "hd",
                "caption": "false",
                "licensedContent": true,
                "regionRestriction": {
                    "allowed": [
                        "KR"
                    ]
                },
                "contentRating": {},
                "projection": "rectangular"
            }
        },
    ],
    "nextPageToken": "CAUQAA",
    "pageInfo": {
        "totalResults": 200,
        "resultsPerPage": 5
    }
}
```


### snippet
제목, 설명, 카테고리 등 동영상에 대한 기본 세부정보
```json
{
  "kind": "youtube#videoListResponse",
  "etag": "d2Ov06VtAJx9m0nFG6MkE96eXJE",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "Wuwwu5iX-GzaCM6jj5w4Jyc5V8Y",
      "id": "rWULE8_Dyt8",
      "snippet": {
        "publishedAt": "2024-04-07T20:03:00Z",
        "channelId": "UCnXNukjRxXGD8aeZGRV-lYg",
        "title": "'결승골 도움' 손흥민… 토트넘 '4위 탈환' #SPOTIME",
        "description": "#손흥민 #도움 #토트넘 #노팅엄\n\n토트넘이 노팅엄을 꺾고 리그 4위로 올라섰습니다\n자세한 내용은 영상으로 확인하시죠~\n\n📺 지금 보고 있는 '이 장면'\nSPOTV NOW에서 시청하실 수 있습니다.\n\nSPOTV NOW ☞ https://www.spotvnow.co.kr/\n내가 원하는 스포츠 상품 구매는? ☞  https://www.spotvmall.com",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/rWULE8_Dyt8/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/rWULE8_Dyt8/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/rWULE8_Dyt8/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/rWULE8_Dyt8/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/rWULE8_Dyt8/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        },
        "channelTitle": "스포타임",
        "tags": [
          "손흥민",
          "토트넘",
          "노팅엄",
          "토트넘 노팅엄 골",
          "토트넘 노팅엄 득점",
          "토트넘 노팅엄 손흥민",
          "손흥민 도움",
          "손흥민 골",
          "손흥민 득점",
          "손흥민 활약",
          "판더벤 골",
          "판 더 펜 골",
          "판 더벤 골",
          "손흥민 이슈",
          "토트넘 노팅엄 하이라이트",
          "토트넘 노팅엄 골 하이라이트",
          "토트넘 노팅엄 리뷰",
          "토트넘 노팅엄 손흥민 골",
          "손흥민 노팅엄 골",
          "손흥민 노팅엄 득점",
          "손흥민 노팅엄 활약상",
          "손흥민 노팅엄 하이라이트",
          "손흥민 노팅엄 9호 도움",
          "손흥민 9호 도움",
          "손흥민 결승골",
          "손흥민 도움왕",
          "손흥민 노팅엄",
          "손흥민 노팅엄전",
          "토트넘 하이라이트",
          "손흥민 하이라이트"
        ],
        "categoryId": "17",
        "liveBroadcastContent": "none",
        "localized": {
          "title": "'결승골 도움' 손흥민… 토트넘 '4위 탈환' #SPOTIME",
          "description": "#손흥민 #도움 #토트넘 #노팅엄\n\n토트넘이 노팅엄을 꺾고 리그 4위로 올라섰습니다\n자세한 내용은 영상으로 확인하시죠~\n\n📺 지금 보고 있는 '이 장면'\nSPOTV NOW에서 시청하실 수 있습니다.\n\nSPOTV NOW ☞ https://www.spotvnow.co.kr/\n내가 원하는 스포츠 상품 구매는? ☞  https://www.spotvmall.com"
        },
        "defaultAudioLanguage": "ko"
      }
    },
  ],
  "nextPageToken": "CAUQAA",
  "pageInfo": {
    "totalResults": 200,
    "resultsPerPage": 5
  }
}
```
### statistics
동영상에 대한 통계
```json
{
  "kind": "youtube#videoListResponse",
  "etag": "aSftgvEgpRJ2XEVU0U-0e_kxxPs",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "ey2iG1YqNJC9f02ZV9PjQ4Ty03Y",
      "id": "aawThz047Bw",
      "statistics": {
        "viewCount": "425203",
        "likeCount": "15085",
        "favoriteCount": "0",
        "commentCount": "261"
      }
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}

```
### topicDetails
동영상과 연결된 주제에 대한 정보
```json
{
  "kind": "youtube#videoListResponse",
  "etag": "f7BS-gQkChGROs2Mwb3mhGr0NQU",
  "items": [
    {
      "kind": "youtube#video",
      "etag": "VrwHUFxqc4CcJ1OMx7TBAj6mOu4",
      "id": "aawThz047Bw"
    }
  ],
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 1
  }
}

```
### fileDetails
파일의 해상도, 재생 시간, 오디오 및 동영상 코덱, 스트림 비트 전송률 등 > 소유자만 검색가능
```json
```
### id
동영상을 고유하게 식별하는 데 사용하는 ID
```json
```
### liveStreamingDetails
동영상이 예정된 방송, 실시간 방송 또는 완료된 실시간 방송인 경우에만 존재하는 정보.
```json
```
### localizations
동영상 메타데이터의 번역
```json
```
### player
동영상을 재생하는 데 사용하는 정보가 포함 > iframe 태그등
```json
```
### processingDetails
업로드된 동영상 파일 처리 과정에서 YouTube의 진행 상황에 대한 정보 > 소유자만 검색가능
```json
```
### recordingDetails
동영상이 녹화된 위치, 날짜, 주소에 대한 정보
```json
```

### status
동영상의 업로드, 처리, 공개 설정 상태에 대한 정보
```json
```
### suggestions
동영상의 동영상 품질 또는 메타데이터를 개선할 수 있는 기회를 식별하는 추천 > 소유자만 검색가능
```json
```

