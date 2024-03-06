<template>
    <div class="flex flex-col justify-center">
        <form v-on:submit.prevent="submitForm" method="post">
            <div class="p-4 flex justify-center">
                <textarea v-model="body" class="w-96 bg-gray-600 text-white rounded-lg" placeholder="What are you thinking about?"></textarea>  
                <button type="submit" class="ml-5 py-4 px-4 bg-blue-400 rounded-lg">Post</button>
            </div> 
        </form>
        <div class ="flex justify-center mb-5"
            v-for="post in posts"
            v-bind:key="post.id"
            >
            <div class="w-[500px] bg-gray-200 flex items-start flex-col rounded-lg shadow-inner ">
                <p class="ml-4 py-3"><strong>{{ post.created_by.username }} </strong> <small class="ml-1">{{ post.created_at_formatted }}</small> </p>
                <p class="w-[440px] ml-7 bg-gray-50 rounded-lg mb-5 py-5 px-3 flex just-start">{{ post.body }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            body: '',
            posts: []
        }
    },
    mounted(){
        this.getPosts()
    },
    methods: {
        getPosts() {
            axios
                .get('/api/posts/')
                .then(response => {
                    this.posts = response.data
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        submitForm() {
            let formData = new FormData()
            formData.append('body', this.body)

            axios
                .post('/api/posts/create/', formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then(response => {
                    this.posts.unshift(response.data)
                    this.body = ''

                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>
