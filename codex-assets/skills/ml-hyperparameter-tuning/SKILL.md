---
name: ml-hyperparameter-tuning
description: >-
  Search hyperparameter spaces efficiently with grid/random/Bayesian/Optuna + early stopping and pruning
---

# ml-hyperparameter-tuning

Find hyperparameters that minimize validation loss. **Grid search:** exhaustive over a discrete grid — only viable for ≤2–3 params (combinatorial blowup). **Random search:** samples randomly — beats grid for the same budget because few params actually matter and random covers more values per important dim (Bergstra & Bengio); good default for a quick pass. **Bayesian optimization (Optuna with TPE, or scikit-optimize):** builds a surrogate model of the objective and proposes promising points — most sample-efficient, the right tool for expensive models/large spaces. Add **pruning/early stopping (Hyperband/ASHA)** to kill unpromising trials early — huge speedup with boosting/NNs. **Best practice:** sample continuous params on log scale (learning_rate, C, reg λ), define realistic ranges, set a trial budget, and tune the few high-impact params first (for GBMs: learning_rate + n_estimators-via-early-stopping, then depth, then subsample/reg). **Critical pitfall:** all tuning must use CV and never touch the final test set — repeatedly peeking overfits the validation set (use nested CV for an honest estimate). Fix random seeds for reproducibility; log every trial.

**Tools:** GridSearchCV, RandomizedSearchCV, Optuna TPE, Hyperband/ASHA, scikit-optimize
