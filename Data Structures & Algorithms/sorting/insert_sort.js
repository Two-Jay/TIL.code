

// * insertion sort (삽입 정렬)

/*
"반복문을 돌면서
대상 배열의 가장 작은 값을 순차적으로 선택하여
왼쪽에 enqueue한다"
*/


/*
    불안정정렬 중 하나, value가 같은 값의 상대적 위치가 변할 수 있다.
    시간복잡도는 O(n^2), 공간복잡도는 O(n)이다.
    입력받은 정렬대상을 제외하고는 그 이상의 공간복잡도를 요구하지 않는다.
    
    K 번째 수를 찾을 때 유용하다. 이 경우 시간복잡도는 O(K*n)이 된다.

    ! 배열이 정렬되어 들어온 경우 최적화 방법
    * 반복문 외부에서 변수를 하나 선언한 후에, 해당 변수를 반복문 조건으로 정한다.
    * 반복문이 시작되면 해당 변수를 초기화시켜서 반복문 조건에 불만족하게 바꾼다.
    * min_index가 바뀌는 시점, 즉 스왑이 일어나는 대상을 포착한 시점에
    * 해당 변수를 반복문 조건에 만족하게 만들어준다.
*/

// 오름차순
function insertion_sort_ascending(array){
    
    let target_array = array.slice();
    let min_index;
    let red_flag = 1;

    for(let i = 0; i < target_array.length && (red_flag === 1); i ++){
        red_flag = 0;
        min_index = i;

        for(let j = i+1; j< target_array.length; j ++){
            if(target_array[j] < target_array[min_index]){
                min_index = j
                red_flag = 1;
                console.log("check")
            }
        }

        [target_array[i], target_array[min_index]] = [target_array[min_index], target_array[i]]
    }

    return target_array
}

// 내림차순
function insertion_sort_descending(array){
    
    let target_array = array.slice();
    let min_index;

    for(let i = 0; i < target_array.length; i ++){
        min_index = i;
        for(let j = i+1; j< target_array.length; j ++){
            if(target_array[j] < target_array[min_index]){
                min_index = j
            }
        }
        [target_array[i], target_array[min_index]] = [target_array[min_index], target_array[i]]
    }

    return target_array
}

// K번째 수 찾기
function insertion_sort_nth(array, num){
    
    let target_array = array.slice();
    let min_index;
    let count = num;

    for(let i = 0; i < count; i++){
        min_index = i;
        for(let j = i+1; j< target_array.length; j ++){
            if(target_array[j] < target_array[min_index]){
                min_index = j
            }
        }
        [target_array[i], target_array[min_index]] = [target_array[min_index], target_array[i]]
    }

    return target_array[count-1]
}