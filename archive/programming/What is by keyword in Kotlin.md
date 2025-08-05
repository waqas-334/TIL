# What is `by` keyword in Kotlin? 
`8 May 2024`

This short explanation can answer the following questions:
1. How to keep you code clean and seperated?
2. How to provide a implementation of an interface in a separate class and use it somewhere else.

Ok so I learned about this really coool thing today called delegation.

And this is how it works:
```
//say you have an interface with ton of functions
interface Foo {
    fun doA()
    fun doB()
    //and much more
} 
```
and you want to implement this `interface` in a `class` but don't want to litter it with all those overloads yet using them as they were there. 

> Here is what you can do:
- Create a new class say `FooDelegate`
- Implement all those methods their and add code as you want
- Use that delegate in the class where you want those implemtation

e.g:
```
class FooDelegate : Foo {

    @override
    fun doA(){
        //do your thing
    }

    @override
    fun doB(){
        //do your thing 
    }

    //and so on
}
```
Now in the class where you want this class to be, just use it as:

```
class ActualClass: Foo by FooDelegate(){
    //that's it
    //now you can call those overrides from anywhere here

    fun ThisClassFunction(){
        //doing something
        doA(); //this will call the overriden function above
    }

}
```

Hope you like it.
And as always, if I find something new regarding this topic, I will add them here. 
Thanks 

~Waqas