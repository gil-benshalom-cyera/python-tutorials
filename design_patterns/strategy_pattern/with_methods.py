import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 2. ModelEvaluator Class
class ModelEvaluator:
    """Context class that applies an evaluation strategy function."""

    def __init__(self, df: pd.DataFrame, strategy=None):
        self.df = df  # Store the dataframe inside the instance
        self.strategy = strategy if strategy else accuracy_evaluation  # Default strategy

    def set_strategy(self, strategy):
        """Allows changing the strategy dynamically."""
        self.strategy = strategy

    def evaluate(self):
        """Applies the evaluation strategy function to itself."""
        return self.strategy(self)  # Pass `self` to the external function



# 1. Define Evaluation Functions Outside the Class
def accuracy_evaluation(evaluator: ModelEvaluator):
    """Evaluates accuracy using the evaluator's stored DataFrame."""
    return accuracy_score(evaluator.df["actual"], evaluator.df["predicted"])


def precision_evaluation(evaluator: ModelEvaluator):
    """Evaluates precision using the evaluator's stored DataFrame."""
    return precision_score(evaluator.df["actual"], evaluator.df["predicted"], average="macro")


def recall_evaluation(evaluator: ModelEvaluator):
    """Evaluates recall using the evaluator's stored DataFrame."""
    return recall_score(evaluator.df["actual"], evaluator.df["predicted"], average="macro")


def f1_evaluation(evaluator: ModelEvaluator):
    """Evaluates F1-score using the evaluator's stored DataFrame."""
    return f1_score(evaluator.df["actual"], evaluator.df["predicted"], average="macro")


def main():
    # Sample DataFrame with model predictions
    data = {
        "actual": [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        "predicted": [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)

    # Instantiate the evaluator with default accuracy strategy
    print(f"Accuracy: {ModelEvaluator(df).evaluate():.2f}")

    # Change strategy dynamically to Precision
    print(f"Precision: {ModelEvaluator(df, precision_evaluation).evaluate():.2f}")

    # Change strategy dynamically to Recall
    print(f"Recall: {ModelEvaluator(df, recall_evaluation).evaluate():.2f}")

    # Change strategy dynamically to F1-score
    print(f"F1-score: {ModelEvaluator(df, f1_evaluation).evaluate():.2f}")


# 3. Usage Example
if __name__ == "__main__":
    main()
