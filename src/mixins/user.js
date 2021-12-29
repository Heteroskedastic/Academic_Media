import { mapGetters , mapActions} from 'vuex'


export const UserMixins = {
    computed: {
        ...mapGetters('user__store', ["Userinfo_getters", "Projects_getters"]),
    },
    methods:{
        ...mapActions('user__store', ["GET_USER_API","GET_USER_Project_ID", "GET_ProjectNews","GET_USER_Project", "POST_USER_Project", "GET_News", 'POST_USER_ProjectNews']),
    }

}