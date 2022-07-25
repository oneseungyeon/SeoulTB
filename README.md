## 연구 내용
매년 취득되고 있는 서울시 유인항공영상으로부터 딥러능을 통해 녹지 픽셀을 탐지해 녹피면적을 산출하고자 하는 프로젝트 

<img src = "https://user-images.githubusercontent.com/74392995/180707734-ae0fab62-3bb4-4971-83fa-7fb43e060a62.png" width = "30%" height = "30%">

## 연구 과정

<img src = "https://user-images.githubusercontent.com/74392995/180711759-182042d0-f947-463f-92d9-2cdae4fc867b.png" width = "70%" height = "40%">

1. 유인항공영상과 비슷한 드론 오픈 데이터셋인 ICG Drone Dataset과 UAVid Semantic Segmentation Dataset에서 tree, low vegetation을 따로 추출하여 사전학습 수행
2. 서울시 중구, 중랑구를 대상으로 녹지 라벨링을 수행하여 pre-trained model을 이용해 fine-tuning 수행
3. 탐지 된 녹지 픽셀을 계산해 공간해상도(GSD)를 고려해 녹피면적과 녹피율 산정

## 딥러닝 모델
DeepResUnet : 종단간 심층 합성곱 신경망(end-to-end DCNN)으로 기존 의미론적 분할 태스크에 많이 이용되는 Unet모델에 Resblock을 추가하여 기존 Unet모델보다 우수한 성능을 보이는 모델

<img src = "https://user-images.githubusercontent.com/74392995/180712016-1e8e34f2-de07-4a45-bbb6-2cadde069206.png" width = "60%" height = "40%">

## 평가 결과
최종 학습이 완료된 모델에 평가데이터셋을 적용하여 평가 데이터셋에 대한 성능 분석 수행
⇒ 녹지의 경우 환경마다 분포 형태와 크기가 다른 객체보다 더 다양하기 때문에 정밀한 녹지 탐지 결과분석을 위해 녹지를 공원, 산, 거주지 주변 녹지, 가로수, 강 주변 녹지로 구분해 평가 수행(Postool, 2013)

<img src = "https://user-images.githubusercontent.com/74392995/180713243-22d41b22-3d3d-48e0-9b2a-701b9a9af37a.png" width = "50%" height = "40%">

## 결론
1. 매년 취득되고 있는 유인항공영상의 이용해 도시녹지 관리의 기초자료로서 녹피율 산정 
2. 두가지 녹지에서 낮은 성능을 보임
- Residual Green Space : 그림자를 식생이라고 인식 ⇒ 과탐지(FP**⬆️**)→ **precision 낮게 측정**

<img src = "https://user-images.githubusercontent.com/74392995/180713034-8ddb4cc5-1276-4359-8841-6a6500ea2e37.png" width = "70%" height = "40%">

- Lake Green Space : 강을 식생이라고 인식 ⇒ 과탐지(FP**⬆️**)→ **precision 낮게 측정**

<img src = "https://user-images.githubusercontent.com/74392995/180713099-46fc8a64-4cd7-458a-80f2-a31fea5b8125.png" width = "70%" height = "40%">
