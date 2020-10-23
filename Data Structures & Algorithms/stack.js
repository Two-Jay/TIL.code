/*

    * 스텍 *

    ? 개요

    임의의 Storage에 Data를 쌓아올리는 자료구조를 말함
    같은 구조와 크기의 자료를 정해진 방향으로만 쌓을 수 있음
    가장 최근에 삽입된 자료로 top 포인터가 정해지고, top 포인터로만 자료를 접근할 수 있음.
    !후입선출(Last In First Out)자료구조

    stack underflow - 빈 스텍에서 자료를 찾는 경우
    stack overflow - storage의 정해진 limit을 넘어서 자료를 push()하는 경우

    Todo 아래의 사항을 구현해 볼 것 
    - 1. pseudoclassical / class stack 구현 
    - 2. .push() .pop()  .size() .search() 구현
    
*/

// Stack structure with array storage on Class
class Stack {
    constructor(stackName, memo){
        this.name = stackName
        this.memo = memo
        this.storage = []
        this.top = null
        this.length = 0
    }

    push(value){
        this.storage.push(value);
        this.length += 1;
        this.top = this.storage[this.length-1];
        return this.length;
    }

    pop(){
        if(this.storage && this.length === 0){
            return undefined;
        }
        let popped = this.storage.pop();
        this.length -= 1;
        return popped;
    }

    size(){
        return this.length;
    }

    contains(value){
        if(!value){
            return false;
        }
        for(let element of this.storage){
            if(element && element === value){
                return true;
            }
        }
        return false;
    }

    info(){
        return { name : this.name, annotation : this.annotation }
    }
}

/*
const stk = new Stack();
console.log(stk)
stk.length() // 0
stk.pop() // undefined
stk.push("a") // 1
stk.push("b") // 2
stk.push("c") // 3
stk.top // "c"
stk.length() // 3
stk.contain("b") // true
stk.contain("d") // false
stk.pop() // "c"
stk.length() // 2
*/

const Stack = function(stackName, memo){
    this.name = stackName;
    this.annotation = memo
    this.storage = [];
    this.top = null;
    this.length = 0;
}

Stack.prototype.push(value){
    this.storage.push(value);
    this.length += 1;
    this.top = this.storage[this.length-1];
    return this.length;
}

Stack.prototype.pop(){
    if(this.storage && this.length === 0){
        return undefiend;
    }
    let popped = this.storage.pop();
    this.length -= 1;
    return popped;
}

Stack.prototype.size(){
    return this.length;
}

Stack.prototype.contains(value){
    if(!value){
        return false;
    }
    for(let element of this.storage){
        if(element && element === value){
            return true;
        }
    }
    return false;
}

// Stack의 이름과 메모를 반환하는 함수를 만들어보았다.
Stack.prototype.info(){
    let info = { name : this.stackName, annotation : this.annotation }
    return info;
}


// Stack structure with object storage on Class
class Stack{
    constructor(){
        this.storage = {}
        this.count = 0
    }

    push(value){
        this.storage[this.count] = value;
        this.count += 1;
        return this.count;
    }

    pop(){
        let popped = this.storage[this.count-1];
        delete this.storage[this.count-1];
        this.count -= 1;
        return popped;
    }

    length(){
        return this.count;
    }

    contains(value){
        if(!value){
            return false;
        }
        for(let element in this.storage){
            if(value === element){
                return true;
            }
        }
        return false;
    }
}

// Todo implementation of Stack structure with limited storage in javascript 
// Todo implementation of Queue structure with two stacks
// Todo implementation of Stack structure with two queues
// Todo implementation of Stack.reverse() which reverses all of the elements in storage