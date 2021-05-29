import pygame,time
_display = pygame.display
COLOR_BLACK = pygame.Color(0,0,0)
COLOR_RED = pygame.Color(255,0,0)
version = 'V1.01'
#游戏主类
class MainGame:
    #游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    #创建我方坦克
    TANK_p1 = None

    def __init__(self):
        pass
    #开始游戏
    def StartGame(self):
        pygame.display.init()
        #创建窗口加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #我方坦克
        MainGame.TANK_p1 = Tank(250,300)
        #设置游戏标题
        _display.set_caption("坦克大战"+version)
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvent()
            #将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d俩"%5),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_p1.displayTank()
            #调用坦克移动方法
            if MainGame.TANK_p1 and not MainGame.TANK_p1.stop:
                MainGame.TANK_p1.move()
            time.sleep(0.02)
            #窗口的刷新
            _display.update()

    #获取程序期间所有事件(鼠标事件，键盘事件)
    def getEvent(self):
        #获取所有事件
        eventList = pygame.event.get()
        #对事件进行判断处理(1，点击关闭按钮2，按下键盘上的某个按键)
        for even in eventList:
            #判断event.type 是否为QUIT,如果时退出的话，直接调用程序结束方法
            if even.type == pygame.QUIT:
                self.EndGame()
            #判断事件类型是否为按键按下，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if even.type == pygame.KEYDOWN:
                #具体是哪个按键的处理
                if even.key == pygame.K_LEFT:
                    print("向左移动")
                    #修改坦克方向
                    MainGame.TANK_p1.direction = "L"
                    MainGame.TANK_p1.stop = False
                    #完成移动操作(调用坦克的移动方法)
                    #MainGame.TANK_p1.move()
                elif even.key == pygame.K_RIGHT:
                    print("向右移动")
                    # 修改坦克方向
                    MainGame.TANK_p1.direction = "R"
                    MainGame.TANK_p1.stop = False
                    #MainGame.TANK_p1.move()
                elif even.key == pygame.K_DOWN:
                    print("向下移动")
                    # 修改坦克方向
                    MainGame.TANK_p1.direction = "D"
                    MainGame.TANK_p1.stop = False
                    #MainGame.TANK_p1.move()
                elif even.key == pygame.K_UP:
                    print("向上移动")
                    # 修改坦克方向
                    MainGame.TANK_p1.direction = "U"
                    MainGame.TANK_p1.stop = False
                    #MainGame.TANK_p1.move()
                elif even.key == pygame.K_SPACE:
                    print("发射子弹")
            if even.type == pygame.KEYUP:
                #松开的如果是方向键，才更改移动开关状态
                if even.key == pygame.K_LEFT or even.key == pygame.K_RIGHT or even.key == pygame.K_UP or even.key == pygame.K_DOWN:
                    MainGame.TANK_p1.stop = True
    #左上角文字绘制的功能
    def getTextSurface(self,text):
        #字体初始化
        pygame.font.init()
        #选择合适的字体
        font = pygame.font.SysFont('kaiti',18)
        #使用对象的字符完成相关的内容绘制
        textSurface = font.render(text,True,COLOR_RED)
        return textSurface
    #结束游戏
    def EndGame(self):
        print("谢谢使用")
        exit()
#坦克类
class Tank:
    def __init__(self,left,top):
        self.images = {
            'U':pygame.image.load('G:/projects/python/tank/images/tanku.png'),
            'D':pygame.image.load("G:/projects/python/tank/images/tankd.png"),
            'L':pygame.image.load("G:/projects/python/tank/images/tankl.png"),
            'R':pygame.image.load("G:/projects/python/tank/images/tankr.png"),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        #坦克所在的区域
        self.rect = self.image.get_rect()
        #指定坦克初始化位置 分别距x,y轴的位置
        self.rect.left = left
        self.rect.top = top
        #新增速度属性
        self.speed = 5
        #新增坦克的移动开关
        self.stop = True
    #坦克移动方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
    #坦克射击类
    def shot(self):
        pass
    #坦克展示(将坦克这个surface绘制到窗口中 blit())
    def displayTank(self):
        #1.重新设置坦克的图片
        self.image = self.images[self.direction]
        #2.将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)
#我方坦克
class MyTank(Tank):
    def __init__(self):
        pass
#地方坦克
class EnemyTank(Tank):
    def __init__(self,left,top,speen):
        pass
#子弹类
class Bullet():
    def __init__(self):
        pass
    #子弹移动方法
    def move(self):
        pass
    #子弹显示方法
    def displayBullet(self):
        pass
#爆炸类
class Explode:
    def __init__(self):
        pass
    #展示爆炸效果
    def displayExplode(self):
        pass
#墙壁类
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
#音效类
class Music():
    def __init__(self):
        pass
    #开始播放音乐
    def play(self):
        pass

MainGame().StartGame()

