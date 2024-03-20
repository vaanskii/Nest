<template>
    <template v-if="userStore.user.isAuthenticated" class="flex justify-center items-center">
      <div class="flex justify-center flex-col items-center mt-10">
        <img :src="user.get_profile_picture" class="w-[150px] h-[150px] rounded-full">
        <h1 class="mt-4"><strong>{{ user.username }}</strong></h1>
      </div>  
      <div class="flex flex-row justify-center space-x-4 mt-8" v-if="user.id">
        <p class="font-bold">
          {{ user.posts_count }} Posts
        </p>
        <RouterLink :to="{ name: 'followers', params: { 'id': user.id }}"
        class="font-bold"
        >
          {{ user.followers_count }} Followers
        </RouterLink>
        <RouterLink
          :to="{ name: 'following', params: { 'id': user.id }}"
          class="font-bold"
        >
          {{ user.following_count }} Following
        </RouterLink>
      </div>
      <div class="flex justify-center">
        <button
          class="py-2 px-2 mb-5 mt-5 bg-black text-white rounded-2xl w-96"
          v-if="userStore.user.id !== user.id"
          @click="toggleFollow"
        >
          {{ user.is_following ? 'Following' : 'Follow' }}
        </button>
        
        <div v-else class="flex flex-row justify-center items-center">
          <RouterLink
          :to="{name: 'editprofile'}"
          class="py-2 px-2 mb-5 mt-5 md:ml-20 bg-black text-white rounded-2xl w-52 md:w-72"
          
        >
          Edit profile
          </RouterLink>
          <div class="menu-right ml-10" v-if="userStore.user.isAuthenticated">
              <a href="#" @click="logout()">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6 text-black">
                  <path fill-rule="evenodd" d="M16.5 3.75a1.5 1.5 0 0 1 1.5 1.5v13.5a1.5 1.5 0 0 1-1.5 1.5h-6a1.5 1.5 0 0 1-1.5-1.5V15a.75.75 0 0 0-1.5 0v3.75a3 3 0 0 0 3 3h6a3 3 0 0 0 3-3V5.25a3 3 0 0 0-3-3h-6a3 3 0 0 0-3 3V9A.75.75 0 1 0 9 9V5.25a1.5 1.5 0 0 1 1.5-1.5h6ZM5.78 8.47a.75.75 0 0 0-1.06 0l-3 3a.75.75 0 0 0 0 1.06l3 3a.75.75 0 0 0 1.06-1.06l-1.72-1.72H15a.75.75 0 0 0 0-1.5H4.06l1.72-1.72a.75.75 0 0 0 0-1.06Z" clip-rule="evenodd" />
                </svg>
              </a> 
          </div>
        </div>

      </div>
      <div class="flex justify-center mt-5">
        <hr class="w-[500px] h-0.5 mx-auto bg-gray-100 border-0 rounded my-3 dark:bg-black mb-5">
      </div>
      <form v-on:submit.prevent="submitForm" method="post" v-if="userStore.user.id === user.id">
            <div class="p-4 flex justify-center mb-10 flex-col items-center">
                <div class="relative w-[240px] md:w-[450px] min-w-[200px] ">
                    <textarea
                        v-model="body"
                        class="peer h-14 w-[200px] md:w-[320px] mr-16 overflow-hidden resize-none border-b border-gray-400 bg-transparent pb-1.5 pt-3 pl-4 font-sans text-sm font-normal text-gray-900 outline outline-0 transition-all focus:border-gray-900 focus:outline-0"
                        placeholder=" "
                        id="text-area"
                    ></textarea>

                    <div id="preview" v-if="url" class="w-[90px] mt-12 absolute">
                            <img :src="url" >
                    </div>
                    <button
                        :disabled="isFormEmpty"
                        type="submit"
                        class="absolute right-0 bottom-0 mb-5 -mr-16 md:mr-2 h-10 w-20 bg-black text-white rounded-2xl"
                    >
                        Post
                    </button>
                    <label
                        for="text-area"
                        class="after:content[' '] pointer-events-none absolute left-0 -top-[12.5px] flex h-full w-full select-none text-[11px] font-normal leading-tight text-blue-gray-500 transition-all after:absolute after:-bottom-1.5 after:left-0 after:w-full after:scale-x-0 after:border-b-[1.5px] after:border-gray-900 after:transition-transform after:duration-300 peer-placeholder-shown:text-sm peer-placeholder-shown:leading-[4.25] peer-placeholder-shown:text-blue-gray-500 peer-focus:text-[11px] peer-focus:leading-tight peer-focus:text-gray-900 peer-focus:after:scale-x-100 peer-focus:after:border-gray-900 peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500"
                    >
                        TWEET FOR NEST
                    </label>
                </div>
                <div class="font-[sans-serif] mt-2 mb-12">
                    <input 
                        type="file" 
                        ref="file" 
                        @change="onFileChange"
                        class="w-full text-black text-sm bg-gray-100 file:cursor-pointer cursor-pointer file:border-0 file:py-2 file:px-4 file:mr-4 file:bg-gray-800 file:hover:bg-gray-700 file:text-white rounded" />
                </div>
            </div>
        </form>
        <div class="flex justify-center mb-5" v-for="(post, index) in posts" :key="post.id">
            <div class="w-[320px] md:w-[500px] bg-transparent border-b-2 mb-10 border-gray-500 rounded-[25px] pb-10 flex items-start flex-col group">
                <div class="flex items-center">
                    <img :src="post.created_by.get_profile_picture" class="w-8 h-8 rounded-full">
                    <RouterLink :to="{name: 'profile', params:{'id': post.created_by.id}}" class="-ml-6 py-3 flex"><strong class="w-[150px] text-black font-medium">{{ post.created_by.username }} </strong>
                    </RouterLink>
                    <div class="flex flex-row ml-20 md:ml-60">
                        <small class=" text-md mr-3 font-mono mt-[1px] text-gray-500">{{ post.created_at_formatted }}</small> 
                        <Dropdown :post="post" :index="index" :getPosts="getUserPosts"/>
                    </div>
                </div>
                <div class="max-w-[420px] mt-2">
                    <p class="w-[280px] md:w-[420px] text-start rounded-lg mb-1 -mt-1 pb-3 pl-10 flex justify-start font-sans break-all">
                    {{ post.body }}
                    </p>
                    <template v-if="post.attachments.length">
                        <img v-for="image in post.attachments" v-bind:key="image.id" :src="image.get_image" class="w-[250px] md:w-[400px] ml-10 mb-4 rounded-xl">
                    </template>
                </div>
                <div class="flex flex-row ml-10 -mb-4">
                    <div>
                        <div class="text-gray-500 text-xs cursor-pointer"  @click="likePost(post.id)">
                            <svg v-if="!post.liked" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-black">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
                          </svg>

                          <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6 text-black">
                            <path d="m11.645 20.91-.007-.003-.022-.012a15.247 15.247 0 0 1-.383-.218 25.18 25.18 0 0 1-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0 1 12 5.052 5.5 5.5 0 0 1 16.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 0 1-4.244 3.17 15.247 15.247 0 0 1-.383.219l-.022.012-.007.004-.003.001a.752.752 0 0 1-.704 0l-.003-.001Z" />
                          </svg>
                        </div>
                    </div>
                    <RouterLink :to="{'name': 'postview', params: {id: post.id}}" class="ml-3">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 0 1-.923 1.785A5.969 5.969 0 0 0 6 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337Z" />
                        </svg>
                    </RouterLink>
                </div>
                <div class="flex flex-row ml-10 mt-7 -mb-4 items-center font-sans">
                    <small class="ml-1">{{ post.likes_count }} likes</small> 
                    <span class=" w-[3px] h-[3px] bg-gray-600 items-center rounded-full ml-1 mr-1"></span>
                    <small class="mr-1">{{ post.comments_count }} replies</small>
                </div>
            </div>
        </div>
    
    </template>
    <template v-else>
      <h1><strong>Please Login to see the profile page</strong></h1>
    </template>
  </template>
  
  <script>
  import { useUserStore } from "@/store/user";
  import { useToastStore } from "@/store/toast";
  import Feed from "@/components/Feed.vue";
  import axios from "axios";
  import Dropdown from "@/components/Dropdown.vue"
  export default {
    setup() {
      const userStore = useUserStore();
      const toastStore = useToastStore();
  
      return {
        userStore,
        toastStore,
      };
    },
    data() {
      return {
        user: {
          id: "",
          is_following: false,
        },
        posts: [],
        body: '',
        isDropdownVisible: null,
        url: null
      };
    },
    components: {
      Feed,
      Dropdown
    },
    mounted() {
      this.getUser();
      this.getUserPosts();
    },
    watch: {
      "$route.params.id": {
        handler: function () {
          this.getUser();
        },
        deep: true,
        immediate: true,
      },
    },
    computed: {
        isFormEmpty() {
            return !this.body && !this.url;
        }
    },
    methods: {
    fetchLikeStatus(id, index) {
        axios
            .get(`/api/posts/${id}/check-like-status/`)
            .then(response => {
                this.posts[index].liked = response.data.isLiked;
            })
            .catch(error => {
                console.error('Error fetching like status:', error);
            });
    },
    onFileChange(e) {
        const file = e.target.files[0];
        this.url = URL.createObjectURL(file);
    },
    logout() {
      this.userStore.removeToken()
      this.$router.push('/login')
    },
    toggleDropdown(index) {
      if (this.isDropdownVisible === index) {
        this.isDropdownVisible = null;
      } else {
        this.isDropdownVisible = index;
      }
    },
    getUser() {
      axios
          .get(`/api/profile/${this.$route.params.id}/`)
          .then((response) => {
            if (response.data.user) {
              this.user = response.data.user;
              this.user.is_following = response.data.is_following;
            } else {
              this.$router.push({ name: 'page404' });
            }
    })
    .catch((error) => {
      if (error.response && error.response.status === 404) {
        this.$router.push({ name: 'page404' });
      } else {
        console.log("error", error);
      }
    });
},
    getUserPosts() {
      axios
          .get(`/api/posts/profile/${this.$route.params.id}/`)
          .then(response => {
            this.posts = response.data.posts;
            this.user = response.data.user;
            // Fetch like status for each post
            this.posts.forEach((post, index) => {
              this.fetchLikeStatus(post.id, index);
            });
          })
          .catch(error => {
            console.error('Error fetching user posts:', error);
          });
      },
    submitForm() {
            let formData = new FormData()
            formData.append('body', this.body)
            formData.append('image', this.$refs.file.files[0])
            axios
                .post('/api/posts/create/', formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    }
                })
                .then(response => {
                    this.posts.unshift(response.data)
                    this.body = ''
                    this.$refs.file.value = null
                    this.$router.go()

                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    toggleFollow() {
      if (this.user.is_following) {
        this.unfollowUser();
      } else {
        this.followUser();
      }
    },
    followUser() {
      axios
        .post(`/api/following/${this.$route.params.id}/follow/`)
        .then((response) => {
          this.user.is_following = true;
          console.log("Followed", response.data);
          this.user.followers_count += 1
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
    unfollowUser() {
      axios
        .post(`/api/following/${this.$route.params.id}/unfollow/`)
        .then((response) => {
          this.user.is_following = false;
          this.user.followers_count -= 1
          console.log("Unfollowed", response.data);
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
    likePost(id) {
  axios
    .post(`/api/posts/${id}/like/`)
    .then(response => {
      const postIndex = this.posts.findIndex(post => post.id === id);

      if (postIndex !== -1) {
        if (response.data.message === 'Liked') {
          this.posts[postIndex].likes_count += 1;
          this.posts[postIndex].liked = true; // Update liked state
        } else if (response.data.message === 'Unliked') {
          this.posts[postIndex].likes_count -= 1;
          this.posts[postIndex].liked = false; // Update liked state
        } else {
          console.log('try again');
        }
      }
    })
    .catch(error => {
      console.log('error', error);
    });
}


  },
  };
  </script>
  