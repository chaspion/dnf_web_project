        $(document).ready(function () {
            console.log('called')
            $("#stat_table").hide();
            showepic();
        });



        function serverID(val) {
            sel = parseInt(val)
            if(sel === 1) {
                return "cain";
            }
            if(sel === 2) {
                return "diregie";
            }
            if(sel === 3) {
                return "siroco";

            }if(sel === 4) {
                return "prey";
            }
            if(sel === 5) {
                return "casillas";
            }
            if(sel === 6) {
                return "hilder";
            }
            if(sel === 7) {
                return "anton";
            }
            if(sel === 8) {
                return "bakal";
            }
        }

        function postCharInfo() {
            let serName = $('#server-name').val();
            let charName = $('#char-name').val();
            let charEncode = encodeURIComponent(charName);
            let dfurl = "https://cors-anywhere.herokuapp.com/https://api.neople.co.kr/df/servers/" + serverID(serName) +
                "/characters?apikey=u24sm4DgTGNKceFknyhar93DXxuHX9pN&characterName=" + charEncode

            if (serName == '선택') {
                alert('서버를 골라주세요');
            } else if (charName == '') {
                alert('캐릭터명을 입력하세요');
                $('#char-name').focus();
            } else {
                alert('검색중입니다')
            }

            $.ajax({
                type: 'POST',
                url: dfurl,
                data: {server_give: serName, name_give: charName},
                success: response => {
                    if (response['result'] == 'success') {
                        alert('검색성공!');
                        window.location.reload();
                    } else {
                        alert('검색실패!');
                    }
                }
            })
        }


        function showCharInfo() {
            $('#df-char').empty();
            $('#df-status').empty();

            let serName = $('#server-name').val();
            let charName = $('#char-name').val();
            let charEncode = encodeURIComponent(charName);
            let dfurl = "https://cors-anywhere.herokuapp.com/https://api.neople.co.kr/df/servers/" + serverID(serName) +
                "/characters?apikey=u24sm4DgTGNKceFknyhar93DXxuHX9pN&characterName=" + charEncode

            if (serName == '선택') {
                alert('서버를 골라주세요');
            } else if (charName == '') {
                alert('캐릭터명을 입력하세요');
                $('#char-name').focus();
            } else {
                alert('검색중입니다')
            }

            $.ajax({
                type: "GET",
                url: dfurl,
                data: {},
                success: (response) => {
                    let charInfo = response["rows"];
                    let charId = charInfo[0]['characterId']
                    let charServer = charInfo[0]['serverId']


                    let charImg = "https://img-api.neople.co.kr/df/servers/" + charServer + "/characters/"
                                    + charId + "?zoom=2"
                    let idurl = "https://cors-anywhere.herokuapp.com/https://api.neople.co.kr/df/servers/" + serverID(serName) + "/characters/" +
                                    charId + "/status?apikey=u24sm4DgTGNKceFknyhar93DXxuHX9pN"




                    $('#img-char').attr("src", charImg);

                    $("#stat_table").show();

                    $.ajax({
                        type: "GET",
                        url: idurl,
                        data: {},
                        success: (response) => {
                            let charInfo2 = response;
                            let status = response['status'];

                            let charName = charInfo2['characterName'];
                            let charClass = charInfo2['jobName'];
                            let charJob = charInfo2['jobGrowName'];
                            let charLevel = charInfo2['level'];
                            let adventureName = charInfo2['adventureName'];
                            let guildName = charInfo2['guildName'];

                            let element = Math.max(status[23]['value'], status[25]['value'],
                                status[27]['value'], status[29]['value'],);

                            if (status[4]['value'] > status[5]['value']) {
                                stat = status[4];
                            } else {
                                stat = status[5];
                            }
                            if (status[10]['value'] > status[11]['value']) {
                                crit = status[10];
                            } else {
                                crit = status[11];
                            }
                            if (element === status[23]['value']) {
                                element_attack = status[23];
                            } else if (element === status[25]['value']) {
                                element_attack = status[25];
                            } else if (element === status[27]['value']) {
                                element_attack = status[27];
                            } else {
                                element_attack = status[29];
                            }
// https://dundam.xyz/view.jsp?server=cain&name=%EC%95%95%EB%8F%84&image=0371060bc18b58a0da2a6f61f79f2e35
                            let dundam_url = "https://dundam.xyz/view.jsp?server=" + serverID(serName) +
                                                "&name=" + charEncode + "&image=" + charId
                            let sirroco = "던파오프 크롤링 필요";
                            let sandbag = "던파오프 크롤링 필요";


                            let charInfo = `<tr><td>${charName}</td><td>${charClass}</td>
                                            <td>${charJob}</td><td>${charLevel}</td>
                                            <td>${adventureName}</td><td>${guildName}</td></tr>`

                            let charStat = `<tr>
                                            <td>${stat['name']} ${stat['value']}</td>
                                            <td>${crit['name'][0]}${crit['name'][3]} ${crit['value']}</td>
                                            <td>${element_attack['name'][0]}${element_attack['name'][1]}${element_attack['name'][4]} ${element_attack['value']}</td>
                                            <td>${sirroco}</td>
                                            <td>${sandbag}</td>
                                            </tr>`

                            $('#df-char').append(charInfo);
                            $('#df-status').append(charStat);
                        }
                    })
                }
            })
        }


        function showepic() {
            $('#item-box').empty();
            $.ajax({
                type: 'GET',
                url: '/api/list',
                data: {},
                success: function (response) {
                    let epics = response['epics'];
                    if (response['result'] == 'success') {
                        for (let i = 0; i < epics.length; i++) {
                            console.log(epics[i]);
                            let name = epics[i]['name'];
                            let channel = epics[i]['channel_name'];
                            let time = epics[i]['time'];
                            let img_url = epics[i]['img_url'];

                            let itemList = `<div class="card">
                                <div class="card-content">
                                  <div class="media">
                                    <div class="media-left">
                                      <figure class="image is-48x48">
                                        <img
                                          src="${img_url}"
                                          alt="Placeholder image"
                                        />
                                      </figure>
                                    </div>
                                    <div class="media-content">
                                      <a target="_blank" class="star-name title is-4">${name}</a>
                                      <p class="subtitle is-6">${channel} ${time}</p>
                                    </div>
                                  </div>
                                </div>
                              </div>`;

                            $('#item-box').append(itemList);

                            console.log('success')
                        }
                    }
                    else {
                        console.log('fail')
                    }
                }
            });
        }
