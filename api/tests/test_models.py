from model import *

# To run: pytest -v

# Dataset loader parameters
url_dados = os.path.join(
    "machine_learning", "data", "golden_dataset_hr_recruitment.csv"
)
colunas = [
    "Age",
    "Gender",
    "EducationLevel",
    "ExperienceYears",
    "PreviousCompanies",
    "DistanceFromCompany",
    "InterviewScore",
    "SkillScore",
    "PersonalityScore",
    "RecruitmentStrategy",
    "HiringDecision",
]

# Load Dataset
dataset = Loader.load_data(url_dados, colunas)
array = dataset.values
X_input = array[:, 0:-1]
y_input = array[:, -1]

# Set default value for scores
BASE_ACCURACY = 0.90
BASE_RECALL = 0.80
BASE_PRECISION = 0.90
BASE_FSCORE = 0.85


def test_model_gradient_booster_with_accuracy():
    """Test Gradient booster model with an accuracy score above the base value"""
    # Import the Gradient Booster pipeline
    gb_path = os.path.join(
        "machine_learning", "pipelines", "hr_recruitment_GBpipeline.pkl"
    )
    pipeline_gb = Pipeline.load_pipeline(gb_path)

    # Get the metrics score
    acuracia_gb = Evaluator.evaluation(pipeline_gb, X_input, y_input)
    recall_gb = Evaluator.evaluation(pipeline_gb, X_input, y_input, "recall")
    precision_gb = Evaluator.evaluation(pipeline_gb, X_input, y_input, "precision")
    fscore_gb = Evaluator.evaluation(pipeline_gb, X_input, y_input, "fscore")

    assert acuracia_gb >= BASE_ACCURACY
    assert recall_gb >= BASE_RECALL
    assert precision_gb >= BASE_PRECISION
    assert fscore_gb >= BASE_FSCORE


def test_model_random_forest_with_accuracy():
    """Test Random Forest model with an accuracy score above the base value"""
    # Import the Random Forest pipeline
    rf_path = os.path.join(
        "machine_learning",
        "pipelines",
        "hr_recruitment_pipeline_test_randomForrest.pkl",
    )
    pipeline_rf = Pipeline.load_pipeline(rf_path)

    # Get the metrics score
    acuracia_rf = Evaluator.evaluation(pipeline_rf, X_input, y_input)
    recall_rf = Evaluator.evaluation(pipeline_rf, X_input, y_input, "recall")
    precision_rf = Evaluator.evaluation(pipeline_rf, X_input, y_input, "precision")
    fscore_rf = Evaluator.evaluation(pipeline_rf, X_input, y_input, "fscore")

    assert acuracia_rf >= BASE_ACCURACY
    assert recall_rf >= BASE_RECALL
    assert precision_rf >= BASE_PRECISION
    assert fscore_rf >= BASE_FSCORE
