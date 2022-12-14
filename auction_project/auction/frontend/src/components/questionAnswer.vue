<template>
    <div>
        <h1>Questions And Answer</h1>
        <!-- Display All questions with the response -->
        {{questions[1].title}}
        <div v-for="q in questions">
            <div>
                <h2>{{ q.title }}</h2>
                <h3>Question: {{ q.description }}</h3>
                <h3>Answer: {{ q.response }} </h3>
                <!-- OWNERID ==user ID IF THIS IS TRUE OUTPUT A BUTTON TO ADD ANSWER! -->
                <div v-if='q.item.owner.username == q.item.user.id'>
                    <div v-if="q.response == '' || q.response == null">
                        <button @click="answerForm(q.id)">Add Answer</button>
                    </div>
                </div>

            </div>
        </div>
        <!-- IF USERID !=OWNER THEN HAVE A BUTTON TO POST A QUESTION (SMALL FORM BOOOM) -->
        <div v-if='item?.owner.id != userId'>
            <h2>Add Question</h2>
            <form>
                <div class="form-input">
                    <h3>
                        <label class="form-label" for="title">Title </label>
                        <input v-model="title" type="text" class="form-control" placeholder="Enter question title">
                    </h3>
                </div>
                <div class="form-input mb-2">
                    <h3><label for="Description">Description</label>
                        <textarea v-model="description" class="form-control" id="Desc" rows="4" required></textarea>
                    </h3>
                </div>
                <button type="submit" class="btn btn-primary mt-4 pt-2 w-50 mb-3" id="b">Submit</button>

            </form>
        </div>
    </div>
</template>


<script lang="ts">
import { onUpdated } from 'vue';

export default {
    props:{
        item:Object,
    },
    data() {
        return {
            questions: [] as any[],
            userId: null,
            title: '',
            description: '',
            check: false,

        }
    },
    methods: {
        async fetch_questions() {
            let response = await fetch("http://localhost:8000/api/questions/");  // NEED to add itemID so it can get all questions from a specific item  (need to add the view for it still)
            let data = await response.json();
            this.questions = data.questions;
            console.log("check" + this.questions)
        },
        //Gets The userID  THAT IS CURRENTLY LOGGED IN!-i dont know if we can current get the user id tho
        async fetch_user() {
            let response = await fetch("http://localhost:8000/user/")
            const data = await response.json();
            this.userId = data.user_id;
        },
        async answerForm(id: any) {

            let response = await fetch("http://localhost:8000/api/questions/" + id + "/");


            //create Answer form

        },
        toggle() {
            this.check = !this.check
        },

        mounted() {
            this.fetch_questions();
        },
    }
}
</script>

<style scoped>

</style>