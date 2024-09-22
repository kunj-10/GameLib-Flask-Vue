// Assigning the create app method of view to createApp constant
const { createApp } = Vue

const TaskApp = {
    data(){
        return {
            task: "",
            tasks: [
                {title: "One"},
                {title: "Two"}
            ]
        }
    },
    delimiters: ['{', '}']
}

// Creating a Vue instance for this TaskApp object
createApp(TaskApp).mount('#app')