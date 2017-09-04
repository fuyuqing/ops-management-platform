$(document).ready(function() {
    $('#edit_form').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
           password: {
                validators: {
                    identical: {
                        field: 'repassword',
                        message: '两次密码不相同'
                    }
                }
            },
            repassword: {
                validators: {

                    identical: {
                        field: 'password',
                        message: '两次密码不相同'
                    },
                }
            },
            ms: {
                validators: {
                    notEmpty: {
                      message:'请填写用户描述信息！'
                    }
                }
            }
        }
    });
});
