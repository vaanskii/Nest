<template>
    <h1><strong>{{ userStore.user.username }}</strong></h1>
    <div class="flex flex-row justify-center">
        <p>500 followers</p>
        <p class="ml-4">25 following</p>
    </div>
    <button class="py-2 px-2 bg-gray-500 rounded-xl">Follow</button>
</template>

<script>
import { useUserStore } from '@/store/user'
import { useToastStore } from '@/store/toast'
import axios from 'axios'
export default{
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore,
            toastStore,
        }
    },

}
</script>