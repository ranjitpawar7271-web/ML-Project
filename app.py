from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            gender = request.form.get('gender')
            race_ethnicity = request.form.get('race_ethnicity')
            parental_level_of_education = request.form.get('parental_level_of_education')
            lunch = request.form.get('lunch')
            test_preparation_course = request.form.get('test_preparation_course')
            reading_score = int(request.form.get('reading_score'))
            writing_score = int(request.form.get('writing_score'))

            data = CustomData(
                gender=gender,
                race_ethnicity=race_ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )

            pred_df = data.get_data_as_dataframe()

            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(pred_df)

            print("Prediction:", result)

            return render_template(
                'home.html',
                result=round(float(result[0]), 2)
            )

        except Exception as e:
            print("Error:", e)
            return render_template('home.html', result="Error occurred")

    else:
        return render_template('home.html', result=None)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

      