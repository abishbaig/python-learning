from typing import List,Dict,Set,Tuple,Any,Optional,Sequence,Callable,TypeVar

# Type Annotations
var: int = 123

# Function Annotations
def add_nums(a: int,b: int,c: int) ->int:
    return a+b+c

# List Type
lst: List[List[int]] = [[1,2,3],[1,2,3]]

# Dict Type
dic: Dict[str,int] = {"Age":22}

# Set Type
mySet: Set[bool] = {True,False,True}

# Tuple Type: Has to define value at each index
myTup1: Tuple[str,str,str] = ("1","2","3")
myTup2: Tuple[Any,Any,Any] = ("1","2","3") # Any Means Can Include any Datatype but in tuple case still error coz have to define type at each index
myTup3: Tuple = ("1","2","3") # Only This Works

# Custom Datatypes
vector = List[int]
vectors = List[vector]
myVect: vector = [1,2,3]
myVects: vectors = [[1,2,3],[4,5,6]]

# Optional Type
def func(output: Optional[bool] = False):
    pass
func()

# Sequence Type: Only List,Tuple as they are ordered and indexable
def myFunc(seq: Sequence[int]):
    pass
myFunc([1,2,3])
myFunc((1,2,3))
# myFunc({1:"A"}) # Not Possible
# myFunc({1,2,3}) # Not Possible

# Callable Type
def addNums(x: int,y: int) -> int:
    return x+y

# ----------------------------------
# Function Accepting an Callable
# def myFuncCall(func: Callable[[int,int], int]) -> int:
#     result = func(1,2)
#     def returnRes(res: int) -> int:
#         return res
#     return returnRes(result)
# funcVar = myFuncCall(addNums)
# print(funcVar)
# ----------------------------------

# Function Returning an Callable
def myFuncCall() -> Callable[[int,int], int]:
    func: Callable[[int,int],int] = lambda x,y: x+y
    return func

funcVar = myFuncCall()
# print(funcVar(1,2))

'''
By using TypeVar, we inform type checkers (like MyPy) that a particular type 
parameter should remain consistent throughout a generic construct. 
For instance, if a function takes an argument of type T and returns a 
value of type T, TypeVar ensures that the input and output types are 
indeed the same.
'''
# Generics
T = TypeVar('T')

def genericType(lst: List[T], index: int) -> T:
    return lst[index]

indexVal = genericType([1,2,"3"], 2)
print(indexVal)

