/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { user } from "@web/core/user";
import { onWillStart } from "@odoo/owl";
import { Chatter } from "@mail/chatter/web/chatter";

patch(Chatter.prototype, {
    setup() {
        super.setup();
        onWillStart(async () => {
            console.log(user)
            console.log(await user.hasGroup('kawiil_financing.group_xyz'))
            this.canSendMessage = await user.hasGroup("kawiil_financing.group_xyz");
        });
    },
});