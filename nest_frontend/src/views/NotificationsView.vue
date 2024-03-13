<template>
    <div class="">
        <div class="flex justify-center items-center flex-col mt-10">
                <div
                    v-for="notification in notifications"
                    v-bind:key="notification.id"
                    v-if="notifications.length"
                    @click="readNotification(notification)"
                    class="mb-5 cursor-pointer"
                    >
                    <div class="p-2 overflow-hidden bg-black py-4 w-[500px] items-center text-indigo-100 leading-none lg:rounded-full flex lg:inline-flex before:ease relative transition-all before:absolute before:right-0 before:top-0 before:h-14 before:w-6 before:translate-x-12 before:rotate-6 before:bg-white before:opacity-15 before:duration-700 hover:shadow-black hover:before:-translate-x-40" role="alert">
                        <span class="flex rounded-full bg-red-500 uppercase px-2 py-1 text-xs font-bold mr-3 ml-5">New</span>
                        <span class="font-semibold mr-2 text-left flex-auto ml-10 text-lg">{{ notification.body }} </span>
                        <svg class="fill-current opacity-75 h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M12.95 10.707l.707-.707L8 4.343 6.586 5.757 10.828 10l-4.242 4.243L8 15.657l4.95-4.95z"/></svg>
                    </div>
                </div>
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-else
            >
                You don't have any unread notifications!
            </div>
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'notifications',

    data() {
        return {
            notifications: []
        }
    },

    mounted() {
        this.getNotifications()
    },

    methods: {
        getNotifications() {
            axios
                .get('/api/notifications/')
                .then(response => {
                    console.log(response.data)

                    this.notifications = response.data
                })
                .catch(error => {
                    console.log('Error: ', error)
                })
        },

        async readNotification(notification) {
    console.log('readNotification', notification.id);

    try {
        const response = await axios.post(`/api/notifications/read/${notification.id}/`);
        console.log(response.data);

        // Check if the required id is present in the notification object
        if (notification.type_of_notification === 'post_like' || notification.type_of_notification === 'post_comment' || notification.type_of_notification === 'comment_like') {
            if (notification.post_id) {
                this.$router.push({ name: 'postview', params: { id: notification.post_id } });
            } else {
                console.error('Error: post_id is missing from the notification object');
            }
        } else {
            if (notification.created_for_id) {
                this.$router.push({ name: 'followers', params: { id: notification.created_for_id } });
            } else {
                console.error('Error: created_for_id is missing from the notification object');
            }
        }
    } catch (error) {
        console.error('Error: ', error);
    }
}

    }
}
</script>