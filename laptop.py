import sys,os,pyautogui,functions,time
pyautogui.PAUSE = 0.6



fname = '......txt'
internal_storage_path = '..............'
filepath = os.path.join(internal_storage_path,fname)
rk = open(filepath)


content = rk.read()
end = content.find(']')
comma = content.find(',')
point = [int(content[1:comma]),int(content[comma+1:end])]
flag = ord(content[end+1])

print(point,"  ",flag)

if flag == 0 :
    pyautogui.moveTo(point[0], point[1], duration=0.25)
else :
    print ("come on ")
    time.sleep(1)
    pyautogui.click(list[0], list[1], button='right')
    print("done")







sys.exit()
