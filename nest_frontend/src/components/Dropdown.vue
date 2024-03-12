<template>
    <div>
        <svg
        xmlns="http://www.w3.org/2000/svg"
        id="dropdownDefaultButton"
        @click="toggleDropdown(index)"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-6 h-6  cursor-pointer"
        >
        <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM18.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
        />
        </svg>
        <div
        v-if="isDropdownVisible === index"
        id="dropdown"
        class="z-10 shadow-lg divide-y divide-gray-100 rounded-lg w-44 bg-gray-100 absolute -ml-40  mt-1 flex justify-center"
        >
        <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownDefaultButton">
            <li v-if="userStore.user.id === post.created_by.id">
            <div
                class="text-xs flex items-center space-x-2  py-4 hover:bg-gray-300 w-[170px] h-[40px] justify-center rounded-lg cursor-pointer"
                @click="deletePost(post.id)"
            >
                <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-5 h-5 text-gray-700"
                >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
                />
                </svg>
                <span class="text-gray-700 font-bold">Delete post</span>
            </div>
            </li>
            <li>
            <div
                class="text-xs flex items-center space-x-2  py-4 hover:bg-gray-300 w-[170px] h-[40px] justify-center rounded-lg cursor-pointer"
            >
                <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-5 h-5 text-gray-700"
                >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M3 3v1.5M3 21v-6m0 0 2.77-.693a9 9 0 0 1 6.208.682l.108.054a9 9 0 0 0 6.086.71l3.114-.732a48.524 48.524 0 0 1-.005-10.499l-3.11.732a9 9 0 0 1-6.085-.711l-.108-.054a9 9 0 0 0-6.208-.682L3 4.5M3 15V4.5"
                />
                </svg>
                <span class="text-gray-700 font-bold">Report post</span>
            </div>
            </li>
        </ul>
        </div>
    </div>
</template>

<script>
  import { useUserStore } from "@/store/user";
  import Feed from "@/components/Feed.vue";
  import axios from "axios";
  export default {
    setup() {
      const userStore = useUserStore();
        
      return {
        userStore,
      };
    },
    props: {
        post: Object,
        index: Number,
        getUserPosts: Function,
        getPosts: Function
    },
    data() {
      return {
        isDropdownVisible: null,
      };
    },

    methods: {
    toggleDropdown(index) {
    if (this.isDropdownVisible === index) {
      this.isDropdownVisible = null;
    } else {
      this.isDropdownVisible = index;
    }
  },
  
    deletePost(postId) {
        axios
          .delete(`/api/posts/${postId}/delete/`)
          .then((response) => {
            console.log(response.data);
            if (typeof this.getUserPosts === 'function') {
              this.getUserPosts();
            }
            if (typeof this.getPosts === 'function') {
              this.getPosts();
            }
            if (this.$route.name === 'postview') {
              this.$router.push('/');
            }
          })
          .catch((error) => {
            console.log('error', error);
          });
      },
  },
  };
  </script>