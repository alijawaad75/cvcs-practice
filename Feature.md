

| No. | Feature               | Simple Purpose                                                                       |
| --- | --------------------- | ------------------------------------------------------------------------------------ |
| 1   | Image Upload          | User handwritten digit ki image upload karega                                        |
| 2   | Digit Prediction      | Model image ko read karke batayega digit `0–9` mein se kaunsa hai                    |
| 3   | Prediction Confidence | Model batayega kitna sure hai, example: `Digit 7 — 96% confidence`                   |
| 4   | Image Preprocessing   | Image ko resize, grayscale, normalize karega taake model easily samajh sake          |
| 5   | Result History        | Previous predictions save hongi, jaise image name, predicted digit, confidence, date |

**Best feature list for report:**

1. **Upload Handwritten Digit Image**
   User system mein handwritten digit image upload karta hai.

2. **Automatic Image Preprocessing**
   System image ko clean, resize, grayscale aur normalize karta hai.

3. **Digit Classification**
   Trained model image ko classify karta hai into digits `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`.

4. **Confidence Score Display**
   System prediction ke sath confidence score show karta hai.

5. **Prediction Record Management using Pandas**
   Pandas prediction history ko table/CSV format mein store karta hai.

