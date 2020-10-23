/*

    * 큐 *

    ? 개요

    임의의 Storage에 Data를 쌓아올리는 자료구조를 말함
    같은 구조와 크기의 자료를 정해진 방향으로만 쌓을 수 있음
    삭제연산이 수행되는 head 포인터와 삽입연산이 수행되는 tail 포인터
    enqueue 시에 tail로 들어가고 dequeue 시에 head로 나옴
    !선입선출(Last In First Out)자료구조

    Todo 아래의 사항을 구현해 볼 것 
    - 1. pseudoclassical / class queue 구현 
    - 2. .enqueue() .dequeue() .size() .contains() 구현

*/

class Queue{
    constructor(){
        this.storage = [];
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    enqueue(value){
        this.storage.push(value);
        this.tail = value;

        //definition of this.head pointer when a value is enqueued first time 
        if(this.head === null && this.size === 0){
            this.head = value;
        }
        this.size += 1;
        return this.size;
    }

    dequeue(){
        // edge case care in case of trying dequeue of the empty queue instance
        if(this.head === null && this.size === 0){
            return undefined;
        }

        let popped = this.storage.pop();
        this.size -= 1;
        this.tail = this.storage[this.size-1] || null;
        
        // edge case care in case of trying to dequeue a last element on storage 
        if(popped && this.size === 0){
            this.head = null;
        }

        return popped;
    }

    length(){
        return this.size;
    }

    contains(value){
        // edge case care in case of trying contains method with an undefined value
        if(!value){
            return false;
        }

        for(let element of this.storage){
            if(element === value){
                return true;
            }
        }
        return false;
    }
}

// Queue structure with an array storage on Pseudofunctional Class
const Queue = function(){
    this.storage = [];
    this.head = null;
    this.tail = null;
    this.size = 0
}

Queue.prototype.enqueue(value){
    this.storage.push(value);
    this.tail = value;
    if(this.head === null && this.size === 0){
        this.head = value;
    } 
    this.size += 1;
    return this.size;
}
Queue.prototype.dequeue(){
    if(this.head === null && this.size === 0){
        return undefined;
    }

    let popped = this.storage.pop();
    this.size -= 1;
    this.tail = this.storage[this.size-1] || null;

    if(popped && this.size === 0){
        this.head = null;
    }

    return popped;
}
Queue.prototype.length(){
    return this.size;
}
Queue.prototype.contains(value){
    if(!value){
        return false;
    }

    for(let element of this.storage){
        if(element === value){
            return true;
        }
    }
    return false;
}

// Todo Queue structure with an object storage on Class
// Todo limited array를 storage로 삼는 스텍 구현 







// 우선순위 큐 구현하기
/*
입력값 [{value : "data_value", priority : "data_priority"}, ...]
예시 [{value : "kim", priority : 2}, {value : "lee", priority : 0}, ...]
우선순위의 최대값은 10으로 한다. 낮은 값 일수록 더 큰 우선순위를 가진다.
*/

class Priority_queue{
    constructor(){
        this.storage = [];
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    enqueue(value, priority){
        if(!value){
            console.log("value를 입력하세요")
            return undefined;
        }
        if(!priority){
            console.log("priority를 입력하세요")
            return undefined;
        }
        if(priority >= 0 && priority < 11){
            let payload = {
                value,
                priority
            }
        }

        this.storage.push(payload);
        this.tail = payload;

        //definition of this.head pointer when a value is enqueued first time 
        if(this.head === null && this.size === 0){
            this.head = payload;
        }
        this.size += 1;
        return this.size;
    }

    dequeue(){
        // edge case care in case of trying dequeue of the empty queue instance
        if(this.head === null && this.size === 0){
            return undefined;
        }

        // check all of element to find the highest priority for dequeue
        let priority_checker = 11
        let popped_index = 0
        for(let i = 0; i < this.size; i++){
            if(this.storage[i]["priority"] < priority_checker){
                priority_checker = this.storage[i][priority]
                popped_index = i
            }
        }

        // execution to dequeue the highest priority element  
        let popped_element = this.storage.slice(popped_index, 1)
        this.size -= 1;
        this.tail = this.storage[this.size-1] || null;
        
        // edge case care in case of trying to dequeue a last element on storage 
        if(popped_element && this.size === 0){
            this.head = null;
        }

        return popped_element;
    }

    length(){
        return this.size;
    }

    contains(value){
        // edge case care in case of trying contains method with an undefined value
        if(!value){
            return false;
        }

        for(let element of this.storage){
            if(element["value"] === value){
                return true;
            }
        }
        return false;
    }
}
