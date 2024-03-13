<template>
    <div class="">
        <div class="main-center col-span-3 space-y-4">
            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="notification in notifications"
                v-bind:key="notification.id"
                v-if="notifications.length"
            >
                {{ notification.body }} 
                <button class="underline" @click="readNotification(notification)">Read more</button>
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