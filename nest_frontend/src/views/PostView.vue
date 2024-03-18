<template>
        <div v-if="post.id" class="flex justify-center flex-col items-center mt-10">
            <div class="w-[480px] bg-transparent border-b-2 mb-10 border-gray-500 rounded-[25px] pb-10 flex items-start flex-col group">
                <div class="flex items-center">
                    <img :src="post.created_by.get_profile_picture" class="w-8 h-8 rounded-full">
                    <RouterLink :to="{name: 'profile', params:{'id': post.created_by.id}}" class="py-3 flex"><strong class=" w-[100px] text-black font-medium">{{ post.created_by.username }} </strong>
                    </RouterLink>
                    <div class="flex flex-row ml-60">
                      <small class="text-md font-mono mr-3 mt-[1px] text-gray-500">{{ post.created_at_formatted }}</small> 
                      <Dropdown :post="post"/>
                    </div>
                </div>
                <div class="max-w-[420px] mt-2">
                    <p class="w-[360px] md:w-[420px] text-start rounded-lg mb-1 -mt-1 pb-3 pl-10 flex justify-start font-sans break-all">
                    {{ post.body }}
                    </p>
                    <template v-if="post.attachments.length">
                        <img v-for="image in post.attachments" v-bind:key="image.id" :src="image.get_image" class="w-[400px] ml-8 mb-4 rounded-xl">
                    </template>
                </div>
                <div class="flex flex-row ml-14 -mb-4">
                    <div class="cursor-pointer" @click="likePost(post.id)">
                        <svg v-if="!post.liked" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                          </svg>

                          <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6 text-black">
                            <path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
                          </svg>
                    </div>
                </div>
                <div class="flex flex-row ml-14 mt-7 -mb-4 items-center font-sans">
                    <small class="ml-1">{{ post.likes_count }} likes</small> 
                    <span class=" w-[3px] h-[3px] bg-gray-600 items-center rounded-full ml-1 mr-1"></span>
                    <small class="mr-1">{{ post.comments_count }} replies</small>
                </div>
            </div>

            <!-- Comment submit form -->
            <div class="bg-white  text-black text-center rounded-lg mt-2">
                <form v-on:submit.prevent="submitForm" method="post">
                    <div class="p-4 flex justify-center mb-10">
                        <div class="relative w-[450px] min-w-[200px]">
                            <textarea
                                v-model="body"
                                class="peer h-14 w-[320px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                                placeholder=" "
                                id="text-area"
                            ></textarea>
                            <button
                                type="submit"
                                class="absolute right-0 bottom-0 mb-5 mr-2 h-10 w-20 bg-black flex justify-center items-center text-white rounded-2xl"
                            >
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                                <path d="M3.478 2.404a.75.75 0 0 0-.926.941l2.432 7.905H13.5a.75.75 0 0 1 0 1.5H4.984l-2.432 7.905a.75.75 0 0 0 .926.94 60.519 60.519 0 0 0 18.445-8.986.75.75 0 0 0 0-1.218A60.517 60.517 0 0 0 3.478 2.404Z" />
                            </svg>
                            </button>
                            <label
                                for="text-area"
                                class="after:content[' '] pointer-events-none absolute left-0 -top-[12.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                            >
                                COMMENT FOR {{ post.created_by.username.toUpperCase() }}
                            </label>
                        </div>
                    </div>
                </form>
            </div>
        

        <!-- Comments -->
        <div v-if="post.comments.length" class="w-[440px] flex justify-center flex-col items-center mb-20">
            <div
            class="border-gray-700 rounded-[25px] w-[400px]"
            v-for="comment in post.comments"
            v-bind:key="comment?.id"
            >
            <hr class="h-0.5 mb-4 bg-black">
            <div  v-if="comment" class="mb-6 flex items-start justify-between flex-col">
                <div class="flex items-center space-x-6">

                    <img :src="comment.created_by.get_profile_picture" class="w-8 h-8 rounded-full">
                    <p>
                        <strong class="text-black mr-4">
                        <RouterLink :to="{name: 'profile', params:{'id': comment.created_by.id}}"> {{ comment.created_by.username }} </RouterLink> 
                        </strong>
                    </p>
                    <div class="flex flex-row items-center">
                        <small class="text-gray-600 font-mono ml-48 text-[12px] font-thin mr-2">{{ comment.created_at_formatted }}</small>
                        <CommentDropdown :comment="comment" :getPost="getPost"/>
                    </div>
                </div>
                <div class="max-w-[390px]">
                    <p class="mt-8 text-start ml-5 text-black font-thin whitespace-pre-line break-words">{{ comment.body }}</p>
                    
                </div>
                <div class="flex flex-row space-x-3 justify-center items-center mt-5 ml-5">
                    <div @click="likeComment(comment.id)" class="cursor-pointer">
                        <svg v-if="!comment.liked" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                          </svg>

                          <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6 text-black">
                            <path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
                          </svg>
                    </div>
                </div>
                <p class="text-[13px] mt-3 ml-5 font-sans">{{ comment.comment_likes_count }} like</p>
            </div>
            </div>
        </div>
        <div v-else>
            <h1 class="text-black uppercase font-bold font-mono">No replies yet... Be first!</h1>
        </div>
    </div>
        
</template>


<script>
import axios from 'axios'
import { useUserStore } from '@/store/user';
import Dropdown from '@/components/Dropdown.vue';
import CommentDropdown from '@/components/CommentDropdown.vue';

export default {
    name: 'PostView',

    setup() {
        const userStore = useUserStore()
        return {
            userStore
        }
    },

    components: {
        Dropdown,
        CommentDropdown
    },

    data() {
        return {
            post: {
                id: null,
                comments: [],
            },
            body: ''
        }
    },

    mounted() {
        this.getPost()
    },

    methods: {
    submitForm() {
        if (!this.body.trim()) {
            return;
        }
        axios
            .post(`/api/posts/${this.$route.params.id}/comment/`, {
                'body': this.body
            }) 
            .then(response => {
                console.log('data', response.data)

                this.post.comments.unshift(response.data)
                this.post.comments_count += 1
                this.body = ''
            })
            .catch(error => {
                console.log('error', error)
            })
    },
    getPost() {
        axios
            .get(`/api/posts/${this.$route.params.id}/`)
            .then(response => {
                console.log('data', response.data)
                this.post = response.data.post
                this.post.comments.forEach(comment => {
                    this.fetchCommentLikeStatus(comment.id)
                });
                this.fetchLikeStatus(this.post.id)
            })
            .catch(error => {
                console.log('error', error)
            })
    },
    fetchCommentLikeStatus(id) {
        axios
            .get(`/api/posts/${id}/check_comment_like/`)
            .then(response => {
                const comment = this.post.comments.find(comment => comment.id === id);
                if (comment) {
                    comment.liked = response.data.isLiked;
                }
            })
            .catch(error => {
                console.log('Error fetching comment like status', error);
            });
    },
    fetchLikeStatus(id) {
        axios
            .get(`/api/posts/${id}/check-like-status/`)
            .then(response => {
                this.post.liked = response.data.isLiked;
            })
            .catch(error => {
                console.error('Error fetching like status:', error);
            });
    },
    likePost(id) {
        axios
            .post(`/api/posts/${id}/like/`)
            .then(response => {
                if (response.data.message === 'Liked') {
                    this.post.likes_count++;
                    this.post.liked = true;
                } else if (response.data.message === 'Unliked') {
                    this.post.likes_count--;
                    this.post.liked = false;
                }
            })
            .catch(error => {
                console.log('error', error);
            });
    },
    likeComment(id) {
        axios
            .post(`/api/posts/${id}/like-comment/`)
            .then(response => {
                const comment = this.post.comments.find(comment => comment.id === id);
                if (comment) {
                    if (response.data.message === 'Liked') {
                        comment.comment_likes_count++;
                        comment.liked = true;
                    } else if (response.data.message === 'Unliked') {
                        comment.comment_likes_count--;
                        comment.liked = false;
                    }
                }
            })
            .catch(error => {
                console.log('error', error);
            });
    }}
}
</script>