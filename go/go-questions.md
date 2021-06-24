# What are the benefits of using Go compared to other languages? 
  * Easy to use due to the single stardard code format. 
  * Optimized for concurrency and works well at scale. 
  * Automatice grabage collection is notablly more efficient than Java or Python

# What form of type conversion does Go support? Convert an integer to float.
# What is a goroutine?
  * A goroutine is a function or method that executes concurrently alongside any other goroutinues using a  special goroutine thread. Goroutine threads are more lightweight than sstandar threads.
  * Can stop a goroutine by sending it a signal channel.

# How do we perform inheritance with Golang.
  * There is no inheritance in golang.
  * Mimic inheritance behavior using composition to use existing struct object to define string behavior of new object. Once the new object be created, functionality can extended beyond the original struct.

# What is interface how do they work.
  * Define a set of method signatures but do not provide implementations.
  * For example, you could implement a geometry interface that defines that all shapes that use this interface must have an implementation of area() and perim().

# What are the looping constructs in GO.
  * Go has only one looping construct: the `for` loop. The loop construct has three components saparated by `;`.
    * The init statement.
    * The condition expression
    * The post statement
    