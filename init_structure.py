import os
import subprocess
import settings


if __name__ == '__main__':
    # inits resource file structure
    os.makedirs(settings.res_dir, exist_ok=True)
    os.makedirs(settings.img_dir, exist_ok=True)
    os.makedirs(settings.dataset_dir, exist_ok=True)
    os.makedirs(settings.result_dir, exist_ok=True)

    # downloads initial given dataset
    bashCommand = "kaggle competitions download -c ds4g-environmental-insights-explorer -p "+str(settings.dataset_dir)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()