<template>
    <div v-if="following.length" class="flex justify-center flex-col items-center mt-5">
        <RouterLink 
            :to="{name: 'profile', params: {'id': user.id}}"
            class="flex flex-row w-[300px]  bg-gray-200 mb-5 h-[50px] items-center rounded-full hover:bg-gray-300"
            v-for="user in following"
            v-bind:key="user.id"    
            >
            <div class="w-7 h-7 bg-black rounded-full ml-2"></div>
            <p class="items-start flex ml-4 text-black w-[100px]">
            <strong>
              <p>{{ user.username }}</p>
            </strong>
          </p>
          <small class="ml-10">{{ user.following_count }} Follower</small>
        </RouterLink>
    </div>
    <div v-else>
        <h1 class="text-black text-lg font-mono font-bold uppercase mt-40">You are not following anyone!
            <br>
            <small>Start following someone to show following list</small>
        </h1>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/store/user'
export default{
    setup() {
        const userStore = useUserStore()

        return {
            userStore,
        }
    },
    data() {
        return {
            user: {},
            following: [],
        }
    },
    mounted() {
        this.getFollowingList()
    },
    methods: {
        getFollowingList() {
            axios
                .get(`/api/following/${this.$route.params.id}/`)
                .then(response => {
                    this.following = response.data.following
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>