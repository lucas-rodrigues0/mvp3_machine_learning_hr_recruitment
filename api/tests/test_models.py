from model import *

# To run: pytest -v

# Dataset loader parameters
url_dados = os.path.join("machine_learning", "data", "test_dataset_hr_recruitment.csv")
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

# Set default value for a base accuracy score
BASE_ACCURACY = 0.90


def test_model_gradient_booster_with_accuracy():
    """Test Gradient booster model with an accuracy score above the base value"""
    # Import the Gradient Booster pipeline
    gb_path = os.path.join(
        "machine_learning", "pipelines", "hr_recruitment_pipeline.pkl"
    )
    pipeline_gb = Pipeline.load_pipeline(gb_path)

    # Get the accuracy score
    acuracia_gb = Evaluator.evaluation(pipeline_gb, X_input, y_input)

    assert acuracia_gb >= BASE_ACCURACY


def test_model_random_forest_with_accuracy():
    """Test Random Forest model with an accuracy score above the base value"""
    # Import the Random Forest pipeline
    rf_path = os.path.join(
        "machine_learning",
        "pipelines",
        "hr_recruitment_pipeline_test_randomForrest.pkl",
    )
    pipeline_rf = Pipeline.load_pipeline(rf_path)

    # Get the accuracy score
    acuracia_rf = Evaluator.evaluation(pipeline_rf, X_input, y_input)

    assert acuracia_rf >= BASE_ACCURACY


def test_model_extra_trees_not_with_accuracy():
    """Test Extra Trees model with an accuracy score below the base value"""
    # Import the Extra Trees pipeline
    et_path = os.path.join(
        "machine_learning", "pipelines", "hr_recruitment_pipeline_test_extraTree.pkl"
    )

    pipeline_et = Pipeline.load_pipeline(et_path)

    # Get the accuracy score
    acuracia_et = Evaluator.evaluation(pipeline_et, X_input, y_input)

    assert not acuracia_et >= BASE_ACCURACY
