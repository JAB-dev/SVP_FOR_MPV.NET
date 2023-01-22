import vapoursynth as vs
#improved version of the script by @SVP4

import vapoursynth as vs
core = vs.core
core.num_threads = 20
#mpv provides display fps so if you want to use that desired_fps=display_fps
#================ CHANGE FPS HERE ==============
desired_fps = 60


#it is recommneded to install the official svp dlls, however newer versions require the manager to be running
# if not hasattr(core,'svp1'):
#     core.std.LoadPlugin("C:\\Program Files (x86)\\SVP 4\\plugins64\\svpflow1_vs.dll")
# if not hasattr(core,'svp2'):
#     core.std.LoadPlugin("C:\\Program Files (x86)\\SVP 4\\plugins64\\svpflow2_vs.dll")

clip = video_in.std.Trim(length=5000000)

super_params     = "{scale:{up:0},gpu:1}"
analyse_params   = "{main:{search:{coarse:{distance:-8,bad:{sad:2000,range:24}},type:2}},refine:[{thsad:250}]}"
#to change fps you need to change num and den, num2,den1 is double the fps 
src_fps     = container_fps if container_fps>0.1 else 23.976



#calculate the num and den for the desired fps
num = round((desired_fps/src_fps) * 100)
den = 100

ratestring = "rate:{num:" + str(num) + ",den:" + str(den) + "}"
smoothfps_params = "{gpuid:11,gpu_qn:2,"+ratestring+",algo:13,mask:{area:100},scene:{}}"



def interpolate(clip):
    input_um = clip.resize.Point(format=vs.YUV420P8,dither_type="random")
    input_m = input_um
    input_m8 = input_m
    smooth  = core.svp2.SmoothFps_NVOF(input_m,smoothfps_params,nvof_src=input_m8,src=input_um,fps=src_fps)
    return smooth

smooth =  interpolate(clip)

smooth.set_output()