from indeed import Get_jobs as Get_ijobs
from save import save_to_file
indeed_jobs=Get_ijobs()

save_to_file(indeed_jobs)
