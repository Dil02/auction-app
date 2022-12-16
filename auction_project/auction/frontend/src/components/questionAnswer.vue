<template>
    <div class="itemBox">
        <!-- Display All questions with the response -->
        <div class="itemBox">
        <h1 class="mx-auto text-align-center w-100 ">Questions And Answer</h1>
        <div v-for="(q, index) in questions" class="question border rounded  pb-3 mb-3 ml-2  me-5" :key="index">
            <div class="w-75">
                <h3 class="title w-100">{{ q.title }}</h3>
                <h5 class="w-100">Description: {{ q.description }}</h5>
                <h5 class="w-100">Answer: {{ q.response }} </h5>
                <!-- OWNERID ==user ID IF THIS IS TRUE OUTPUT A BUTTON TO ADD ANSWER! -->
                <div v-show='(check == false)'>
                    <div v-if="q.response == '' || q.response == null">
                        <form v-on:submit.prevent="updateQuestion(q.id, q, index)"
                            class="sq d-flex-inline flex-column justify-content-center mx-auto w-100 inline">
                            <div><textarea v-model="response[index]" class="form-control w-75 ml-auto mx-auto"
                                    rows="4"></textarea></div>
                            <div><button type="submit" class="btn btn-primary  w-75 pt-2 w-50 mb-3 mx-auto mt-2 d-block"
                                    id="c">Submit</button></div>
                        </form>
                    </div>
                </div>

            </div>
            </div>
        </div>
        <!-- IF USERID !=OWNER THEN HAVE A BUTTON TO POST A QUESTION (SMALL FORM BOOOM) -->

        <div v-if="check">
            <form v-on:submit.prevent="SaveQuestion" class="sq d-flex flex-column justify-content-center mx-auto w-50 p-3">
                <h2 class="q-t">Add Question</h2>
                <div class="form-input">
                    <h3>
                        <label class="form-label" for="title">Title</label>
                        <input v-model="title" type="text" class="form-control w-100 text"
                            placeholder="Enter question title">
                    </h3>
                </div>
                <div class="form-input mb-2">
                    <h3><label for="Description">Description</label>
                        <textarea v-model="description" class="form-control" id="Desc" rows="4" required></textarea>
                    </h3>
                </div>
                <button type="submit" class="btn btn-primary  pt-2 w-50 mb-3 mx-auto" id="b">Submit</button>


            </form>
        </div>
    </div>
</template>


<script lang="ts">
type Question = {
    title: string;
    description: string;
    response: String;
    id: Number;
};
function getCookie(name: String): string {
    let cookieValue = "";
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
export default {
    data() {
        return {
            questions: [] as Array<Question>,
            userId: null,
            title: '',
            description: '',
            check: false,
            ownerId: null,
            valid: true,
            valid2: false,
            response: [],
            item: null,
        }
    },
    methods: {

        async fetch_item(): Promise<void> {
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id);
            let data = await response.json();
            this.item = data.item;
            this.ownerId = data.item.owner.id;
        },
        async fetch_questions(): Promise<void> {
            let response = await fetch("http://127.0.0.1:8000/api/items/" + this.$route.params.id + "/questions", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" });  // NEED to add itemID so it can get all questions from a specific item  (need to add the view for it still)
            let data = await response.json();
            this.questions = data.questions;
        },
        //Gets The userID  THAT IS CURRENTLY LOGGED IN!
        async fetch_user(): Promise<void> {
            let response = await fetch("http://127.0.0.1:8000/api/sessionUser/", { credentials: "include", mode: "cors", referrerPolicy: "no-referrer" })
            const data = await response.json();
            this.userId = data.User.id;
        },
        async SaveQuestion(): Promise<void> {
            const question = JSON.stringify({
                title: this.title,
                description: this.description,
                item: this.$route.params.id,
                response: '',
            })
            let response = await fetch("http://127.0.0.1:8000/api/questions/", {
                method: 'POST',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie("csrftoken"),
                },
                body: question,
            })
            this.fetch_questions();
        },
        async updateQuestion(id: Number, q: Question, index: number): Promise<void> {
            const question = JSON.stringify({
                title: q.title,
                description: q.description,
                item: this.$route.params.id,
                response: this.response[index],
            })

            let response = await fetch("http://127.0.0.1:8000/api/questions/" + id + "/", {
                method: 'PUT',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie("csrftoken"),
                },
                body: question,
            })
            this.fetch_questions();
        },
    },
    async mounted(): Promise<void> {
        this.fetch_item();
        this.fetch_user();
        this.fetch_questions();
    },
    computed: {
        check: function (): boolean {
            if (this.userId == this.ownerId) {
                return false;
            }
            return true
        },

    }

}
</script>

<style scoped>

.title {
    font-weight: bold;
    color: rgb(30, 166, 251);


}

.question {
    justify-content: space-evenly;
    color: white;
    background-color: #141313;
    width:55em;
    margin: auto auto;
    display:flex;

}

.sq {
    color: rgb(0, 0, 0);
    background-color: #ffffff;
    border-radius: 3%;
    margin-bottom: 2%;
}
.itemBox {
    border-color: solid  #008148 !important;
    background-color: #212529 !important;
    height: auto;
    color: white;
    text-align: center;
    display:flex;
    justify-content:center;
    flex-direction: column;
    gap:5;
    border-radius:1em;
}
.q-t{
    text-align: center
}
#Desc ,.text{
    border:solid;
}
</style>