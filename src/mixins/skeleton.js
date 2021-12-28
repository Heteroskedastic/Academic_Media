import { mapGetters , mapActions} from 'vuex'

export const SkeletonMixins = {
    computed: {
        ...mapGetters('skelton__store', ["drawer_getters"]),

        ComputedDrawer: {
            get() {
                return this.drawer_getters
            },
            set(newName) {
                return this.ChangeDrawer(newName)
            }
        },

    },
    filters: {
        uppercase: function(v) {
          return v.toUpperCase();
        }
      },
    methods:{
        ...mapActions('skelton__store', ["ChangeDrawer"]),

        ChangeDrawer_mixin(value){
            this.ChangeDrawer(value)
        }
    }
}