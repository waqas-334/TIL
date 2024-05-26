# How to use Turbine to test Flows in Android.

`19th May 2024`

Testing flows can get challenging. Specifcially, when we to test each item that is sent through the flow.
Here this amazing library called [Tubrine](https://github.com/cashapp/turbine) comes to rescue. Is is developed by CashApp.

So here is how it works. 

Suppose you have this `ProfileViewModel` which have a function that loads the user. It emits the state using a data class called `ProfileState`:
```
data class ProfileState(
    val profile: Profile? = null,
    val isLoading: Boolean = false,
    val errorMessage: String? = null
)
```
And the function that loads this profile looks like this:
```
class ProfileViewModel(private val repo: Repository){

    private val _state = MutableStateFlow(ProfileState())
    val state = _state.asStateFlow()


    //...
    fun loadProfile(){
        viewmodelScope.launch{
            _state.update{it.copy(isLoading = true)}

            val profile = repo.getProfile("someID);

            _state.update{
                it.copy(
                    profile = result.getOrNull(),
                    isLoading = false,
                    errorMessage = profille.exceptionOrNull()?.message
                    )
            }
        }
    }
}
```
It just loads the data and updated the state flow.

## Writing Unit Test for this.

As usual we will create a test class in the Unit Test Resource directory and call it `ProfileViewModelTest`

```
class ProfileViewModelTest{
    private lateinit var viewmodel: ProfileViewModel
    private lateinit var repository: Repo 

    @Before
    fun setup(){
        repository = FakeRepo()
        viewmodel = ProfileViewModel(repository)

        val testDispatcher: TestDispatcher = StandardTestDispatcher() //why
        Dispatchers.setMain(testDispatcher) //why
    }

    //question why we use runTest?
    @Test
    fun `Test loading state update`() = runTest{
        //this is how flow testing starts
        viewmodel.state.test{
            //first we make sure that it shows correct state
            val emission1 = awaitItem() 
            //above will suspend the execution until an item in viewmodel.state is observer
            //once program proceeds we are sure that emission1 will have the first emission
            //so we test that first
            assertThat(emission1.isLoading).isFalse()

            //now we load the profile and see if the state updates accordingly
            viewmodel.loadProfile()

            //now we get the next Item using the same function
            val emission2 = awaitItem()

            //test that
            assertThat(emission2.isLoading).isTrue() //it should be true


            //final emission
            val emission3 = awaitItem()
            assertThat(emission3.isLoading).isFalse()

        }
    }

}
```

> **NOTE:** `assertThat`, `isTrue` etc comes from [AssertK Library](https://github.com/willowtreeapps/assertk) but you can use any library for validation

> **NOTE:** `TestDispatcher` and `StanderdTestDispatcher` comes from [`kotlin-coroutine-test`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/) library

> **FINAL NOTE:** Will also explain in future all the whys in the code.

Cheers

PS: The follow repos could be helpful:
- https://github.com/philipplackner/TestingCourse/tree/part7.4/testing_flows_initial
- https://github.com/philipplackner/TestingCourse/tree/part7.4/testing_flows_final