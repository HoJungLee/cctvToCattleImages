# 링크드 리스트 기반
# 추적기 시간 복잡도는 O(n)

# id 값임
global iden
iden = 0


class Node:
    def __init__(self, x,y,len):
        global iden
        iden = iden + 1
        self.id = iden #  id
        self.x = x # 중앙 값에 x좌표
        self.y = y # 중앙 값에 y좌표
        self.len = len # 업데이트를 결정하는 최소 거리 기준
        self.age = 0 # 노드의 수명을 결정하는 나이
        self.ref = None # 다음 노드


class LinkedList:
    def __init__(self):
        self.start_node = None

    def display(self):
        if(self.start_node == None):
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.x , "<- x ")
                print(n.id," <- id")
                n = n.ref

    # 새로운 값 등록 시
    def insert(self, x,y,len):
        new_node = Node(x,y,len)

        if(self.start_node == None):
            self.start_node = new_node
            return new_node.id
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node
        return new_node.id

    #변경
    def update(self, index, x ,y , len):
        n = self.start_node
        for i in range(0,index):
            n= n.ref
        n.x = x
        n.y = y
        n.len = len
        n.age = 0
        return n.id


    def delete(self,index):
        if( index == 0):
            self.start_node = self.start_node.ref
            return

        pre = None
        n = self.start_node

        for i in range(0,index):
            pre = n
            n = n.ref

        pre.ref = n.ref


    #나이 들기  20번 이상 감지 안되면 죽음
    def old(self):
        n = self.start_node
        index = 0
        while n is not None:
            n.age += 1
            if(n.age >= 20):
                self.delete(index)
            n = n.ref
            index += 1





    #최소값 찾아서 연결하기
    def closer(self , x1, x2, y1 ,y2 ):

        # 길이
        w = x2 - x1
        h = y2 - y1

        # 박스의 중앙 값
        nx = x2 - w/2
        ny = y2 - h/2

        nlen = ( w  + h ) / 4

        # 리스트가 비어 있을 경우
        n = self.start_node
        if( n == None):
            return self.insert(nx,ny,nlen)

        temp = -1
        tmin = None

        index = 0 # 순서
        while n is not None:
            tempLen =  np.sqrt( (n.x - nx) * (n.x - nx) + (n.y - ny) * (n.y - ny ) ) # 거리 계산
            tempLen = float(tempLen)

            if tmin is None:
                tmin = tempLen


            if(tempLen <= tmin and tempLen <= n.len ):
                temp = index

            index += 1;
            n = n.ref

        # 판정 결과
        if( temp == -1):
            return self.insert(nx,ny,nlen) # 새로 만들어
        else:
            return self.update(temp,nx,ny,nlen) # 기존 것 
