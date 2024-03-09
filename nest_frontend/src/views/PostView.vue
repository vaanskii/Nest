<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <div class="main-center col-span-3 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 text-start rounded-lg"
                v-if="post.id"
                >
                <Feed v-bind:post="post"></Feed>
            </div>


        </div>
    </div>
</template>


<script>
import axios from 'axios'
import Feed from '@/components/Feed.vue';

export default {
    name: 'PostView',

    components: {
         Feed,
    },

    data() {
        return {
            post: {
                id: null,
            },
            body: ''
        }
    },

    mounted() {
        this.getPost()
    },

    methods: {
        getPost() {
            axios
                .get(`/api/posts/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)
                    this.post = response.data.post
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
        },
    }
</script>