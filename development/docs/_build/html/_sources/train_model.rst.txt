Train Model
=======================

This is the first function that should be used after collecting training data. It calls :meth:`clean_training_data()` to correctly format the data placed in the :file:`surrender20/development/data/interim` directory. It then creates the model and stores it in pickle files that are used by :meth:`predict_response()`.

.. automodule:: train_model
	:members: