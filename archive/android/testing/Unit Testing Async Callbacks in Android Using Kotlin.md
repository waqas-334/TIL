# How to unit test async callbacks in Android/Kotlin 
`6th May 2024`

## Problem
I need to test a class that uses `Builder` pattern and accepts callbacks to triger when succeed.
I need to know if the callback with correct params is triggered or not. 

As the callbacks are async so the class can take some time to respond, and I need to wait for that.

### Code
```
class UserIdGenerator private constructor(val builder: UserIdGenerator.Builder){

    fun generate(){

    }
}
```

it's getting too long, will complete later. 
`7th May 2024`
