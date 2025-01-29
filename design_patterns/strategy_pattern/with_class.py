from abc import ABC, abstractmethod
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# 1. Strategy Interface
class EvaluationStrategy(ABC):
    """Abstract base class for evaluation strategies."""

    @abstractmethod
    def evaluate(self, y_true, y_pred):
        pass


# 2. Concrete Strategies
class AccuracyEvaluation(EvaluationStrategy):
    """Concrete Strategy: Computes Accuracy."""

    def evaluate(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)


class PrecisionEvaluation(EvaluationStrategy):
    """Concrete Strategy: Computes Precision."""

    def evaluate(self, y_true, y_pred):
        return precision_score(y_true, y_pred, average="macro")


class RecallEvaluation(EvaluationStrategy):
    """Concrete Strategy: Computes Recall."""

    def evaluate(self, y_true, y_pred):
        return recall_score(y_true, y_pred, average="macro")


class F1Evaluation(EvaluationStrategy):
    """Concrete Strategy: Computes F1-score."""

    def evaluate(self, y_true, y_pred):
        return f1_score(y_true, y_pred, average="macro")


# 3. Context Class
class ModelEvaluator:
    """Context class that applies the selected evaluation strategy."""

    def __init__(self, strategy: EvaluationStrategy):
        self.strategy = strategy  # Injecting evaluation strategy

    def set_strategy(self, strategy: EvaluationStrategy):
        """Allows changing the strategy dynamically."""
        self.strategy = strategy

    def evaluate(self, df: pd.DataFrame):
        """Applies the evaluation strategy on the given DataFrame."""
        y_true = df["actual"]
        y_pred = df["predicted"]
        return self.strategy.evaluate(y_true, y_pred)


# 4. Usage Example
if __name__ == "__main__":
    # Sample DataFrame with model predictions
    data = {
        "actual": [1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        "predicted": [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)

    # Use different evaluation strategies
    evaluator = ModelEvaluator(AccuracyEvaluation())
    print(f"Accuracy: {evaluator.evaluate(df):.2f}")

    evaluator.set_strategy(PrecisionEvaluation())
    print(f"Precision: {evaluator.evaluate(df):.2f}")

    evaluator.set_strategy(RecallEvaluation())
    print(f"Recall: {evaluator.evaluate(df):.2f}")

    evaluator.set_strategy(F1Evaluation())
    print(f"F1-score: {evaluator.evaluate(df):.2f}")
