Face tracking use Opencv Tracker

### Tracker Types
`['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'CSRT', 'MOSSE']`

- BOOSTING a good object tracker, seems always tracking, even object changed in ROI
- MIL like BOOSTING, seems always tracking, even object changed in ROI
- KCF can be effected by the changed object in ROI, high process speed up to official doc
- TLD can be effected by the changed object in ROI, seems worse than KCF in face tracking
- MEDIANFLOW accuracy better performance than KCF in face tracking
- GOTURN cv2.error: OpenCV(3.4.1) /Users/travis/build/skvark/opencv-python/opencv/modules/dnn/src/caffe/caffe_io.cpp:1119: error: (-2) FAILED: fs.is_open(). Can't open "goturn.prototxt" in function ReadProtoFromTextFile
- CSRT seems always tracking, even object changed in ROI
- MOSSE seems always tracking, even object changed in ROI


> KCF, MEDIANFLOW, TLD can be used for face tracking, MEDIANFLOW, KCF, TLD shows the decreasing accuracy performance


