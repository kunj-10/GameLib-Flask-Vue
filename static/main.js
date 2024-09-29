// Assigning the create app method of view to createApp constant
const { createApp } = Vue

const TaskApp = {
    data(){
        return {
            task: {
                'title': ''
            },
            tasks: []
        }
    },
    async created(){
        await this.getTasks()
    },
    methods: {
        async getTasks(){
            const response = await fetch(window.location, {
                method: 'get',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })

            this.tasks = await response.json()
        },
        async createTask(){
            
            await this.getTasks()

            const response = await fetch(window.location + 'create',{
                method: 'post',
                headers: {
                    'Content-type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify(this.task)
            })

            await this.getTasks()
        }
    },
    delimiters: ['{', '}']
}

// Creating a Vue instance for this TaskApp object
createApp(TaskApp).mount('#app')