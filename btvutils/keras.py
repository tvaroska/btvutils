from tensorflow.keras.callbacks import Callback

class TrainingPlot(Callback):
    def on_train_begin(self, logs):
        self.metrics = {}
        return super().on_train_begin(logs=logs)

    def on_epoch_end(self, epoch, logs):

        for metric in logs.keys():
            if metric not in self.metrics.keys():
                self.metrics[metric] = [None] * epoch
            self.metrics[metric].append(logs.get(metric))

        # TODO: plot graph if on Notebook
        # TODO: storage images to directory/GCS if in script
        #print(self.metrics)

        return super().on_epoch_end(epoch, logs=logs)