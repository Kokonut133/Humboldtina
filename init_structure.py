import os
import settings
import subprocess
import zipfile

if __name__ == '__main__':
    # inits resource file structure
    os.makedirs(settings.res_dir, exist_ok=True)
    os.makedirs(settings.img_dir, exist_ok=True)
    os.makedirs(settings.dataset_dir, exist_ok=True)
    os.makedirs(settings.result_dir, exist_ok=True)
    os.makedirs(settings.random_dir, exist_ok=True)


    # downloads initial given dataset and unzips
    ds4g_dir = os.path.join(settings.dataset_dir, "ds4g-environmental-insights-explorer")
    if not os.path.exists(ds4g_dir):
        bashCommand = "kaggle competitions download -c ds4g-environmental-insights-explorer -p " + str(settings.dataset_dir)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        with zipfile.ZipFile(ds4g_dir+".zip", 'r') as zip_ref:
            zip_ref.extractall(ds4g_dir)
        os.remove(ds4g_dir+".zip")
