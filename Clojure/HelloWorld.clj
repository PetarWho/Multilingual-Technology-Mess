(ns clojure.examples.hello
	(:gen-class))

(defn hello-world [username]
(println (format "Hello, %s" username)))

(hello-world "world")

(loop [num (read-line)]
   (if (= num "69") (do (hello-world "world in a loop")) (do (println "Type 69 for the result..") (recur (read-line))))
)

(println "")
(println "End of program...")
