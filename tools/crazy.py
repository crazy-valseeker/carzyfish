# -*- coding:utf-8 -*-
import traceback
import os



class StringOperator:
    def __init__(self):
        pass

    def checkHasEnterInTail(self, str_in):
        if len(str_in) < 2:
            return False
        if str_in[-1] == 'n' and str_in[-2] == '\\':
            return True
        return False

    def getStrHasEnterInTail(self, str_in):
        str_out = str_in
        if self.checkHasEnterInTail(str_in) == False:
            str_out += '\n'
        return str_out



class FileDirOperator:
    def __init__(self):
        pass

    def getContentFromFile(self, fPath):
        """
        功能：输入文件完整路径，获取文件内容
        Args:
            fPath: 文件的完整路径
            eg: 'd:\\xx.txt'
                'd:\\yy.cpp'
        Returns:
            内容列表 [list]
            eg: ['hello\n', 'world\n']
        """
        fHanle = open(fPath, 'r')

        # 获取文件内容
        # eg: ['hello\n', 'world\n']
        res = fHanle.readlines()

        fHanle.close()

        return res

    def getAllFilesFromDir(self, dirPath):
        """
            功能：提取某个目录下所有文件（目录下有目录, 文件）
        Args:
            dirPath: 待提取的目录
                eg: 'c:\\test1'
        Returns:
             文件列表（完整路径）
                eg: ['c:\\Green\\app.ico', 'c:\\Green\\mod.ini']
        """
        # 存放dirPath下所有文件的完整路径
        # eg: ['c:\\Green\\app.ico', 'c:\\Green\\mod.ini']
        res = []

        # 走遍dirPath下的每一个目录，得到每一个目录下的目录列表、文件列表
        # eg: dirPath = 'c:\\Green'
        #     ('c:\\Green', ['logs', 'routes'], ['app.ico', mod.ini'])
        #     ('c:\\Green\\logs', [], [])
        #     ('c:\\Green\\routes', ['hello'], [])
        #     ('c:\\Green\\routes\\hello', [], [])
        for root, dirs, files in os.walk(dirPath):
            # 遍历文件列表
            for f in files:
                # 得到文件的完整路径
                res.append(os.path.join(root, f))

        # 遍历完毕，返回结果
        return res

    def createFile(self, filePath):
        if os.path.isfile(filePath) == False:
            dirPath, fileName = os.path.split(filePath)
            os.makedirs(dirPath)
            fHandle = open(filePath[:-1], 'w')
            fHandle.close()

    def writeFile(self, filePath, contentList):
        fHandle = open(filePath[:-1], 'w')
        fHandle.writelines(contentList)
        fHandle.close()

class DirTxtConverter:
    def __init__(self):
        # 目录/文件操作工具
        self.f_d_operator = FileDirOperator()

        # 字符串操作工具
        self.str_operator = StringOperator()

    def Dir2Txt(self, dirPath):
        # 得到所有的文件完整路径
        fPathList = self.f_d_operator.getAllFilesFromDir(dirPath)

        for fPath in fPathList:
            contentList = self.f_d_operator.getContentFromFile(fPath)

            if contentList == []:
                contentList.append('\n')
            else:
                contentList[-1] = self.str_operator.getStrHasEnterInTail(contentList[-1])

            contentList.insert(0, '===crazybegin\n')
            contentList.insert(1, fPath + '\n')
            contentList.append('===crazyend\n')

            f = open(os.path.join(dirPath, 'crazy.txt'), 'a')
            f.writelines(contentList)
            f.close()

    def Txt2Dir(self, txtPath):
        fHandle = open(txtPath, 'r')
        res_init = fHandle.readlines()
        res_out = []
        res_temp = []
        for content in res_init:
            res_temp.append(content)
            if content == '===crazyend\n':
                res_out.append(res_temp)
                res_temp = []
        for cc in res_out:
            cc.pop(0)
            cc.pop(-1)
            filePath = cc[0]
            cc.pop(0)
            self.f_d_operator.createFile(filePath)
            self.f_d_operator.writeFile(filePath, cc)
class Asker:
    def __init__(self):
        # 目录txt转化工具
        self.d_t_converter = DirTxtConverter()

    def input_1(self):
        """
        功能：输入1 or 2，指示进行压缩or 解压。

        Returns:'1' or '2'
            '1'：目录下所有文件内容压缩到txt文件中
            '2'：将txt文件内容解压成一个完整目录
        """
        r_in = raw_input('请输入1（目录 -> txt）或2（txt -> 目录）：')

        while r_in not in ['1', '2']:
            r_in = raw_input('请输入1（目录 -> txt）或2（txt -> 目录）：')

        return r_in

    def input_2(self, ope):
        """
        功能：
        Args:
            ope: 'dir' or 'txt'
                'dir'：获取用户输入的目录路径
                'txt'：获取用户输入的txt 完整路径
        Returns:
            路径
            eg: 'c:\helloWorld'
                'c:\helloWorld\Test.txt'
        """
        while True:
            # todo 增加确认confirm y/n
            if ope == 'dir':
                r_in = raw_input('请输入目录路径（eg: c:\helloWorld）：')
            elif ope == 'txt':
                r_in = raw_input('请输入txt文件完整路径（eg: c:\helloWorld\Test.txt）：')

            if os.path.exists(r_in) == True:
                if ope == 'dir' and os.path.isdir(r_in) == True:
                    break
                elif ope == 'txt' and os.path.isfile(r_in) == True:
                    # todo 判断是txt
                    break
        return r_in

    def run(self):
        """
        功能：通过命令行交互指示用户操作
        """
        # '1' or '2'
        r_in = self.input_1()

        # 目录 -> txt
        if '1' == r_in:
            # 路径
            dirPath_in = self.input_2('dir')

            # 目录 -> txt
            self.d_t_converter.Dir2Txt(dirPath_in)

        # txt -> 目录
        elif '2' == r_in:
            # 路径
            txtPath_in = self.input_2('txt')

            # txt -> 目录
            self.d_t_converter.Txt2Dir(txtPath_in)
        else:
            pass


if __name__ == '__main__':
    try:
        app1 = Asker()
        app1.run()

    except Exception, e:
        traceback.print_exc()
