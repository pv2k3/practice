var container = document.getElementById("content");
async function blink(inner_line, n) {
    let dotted = document.getElementsByClassName("trans");
    setTimeout(() => {
        inner_line.innerHTML += "<span class=\"trans\">...</span>";
        setTimeout(() => {
            dotted[n].style.color = "green";
            setTimeout(() => {
                dotted[n].style.color = "cyan";
                setTimeout(() => {
                    dotted[n].style.color = "yellow";
                    setTimeout(() => {
                        dotted[n].style.color = "green";
                    }, 500)
                }, 500)
            }, 500)
        }, 500)
    }, 500)
}

// blink();

async function insert(func) {
    let inner = document.getElementsByClassName("inner_line");
    container.innerHTML += "<p class=\"inner_line\">Initializing hacking</p>";
    await func(inner[0],0);
    setTimeout(async () => {
        container.innerHTML += "<p class=\"inner_line\">Accessing your files</p>";
        await func(inner[1],1);
        setTimeout(async () => {
            container.innerHTML += "<p class=\"inner_line\">Sending your passwords and files to server</p>";
            await func(inner[2],2);
            setTimeout(async () => {
                container.innerHTML += "<p class=\"inner_line\">Your system hacked</p>";
                await func(inner[3],3);
                setTimeout(async () => {
                    container.innerHTML += "<p class=\"inner_line\">Exiting the console</p>";
                    await func(inner[4],4);
                }, 3000);
            }, 3000);
        }, 3000);
    }, 3000);
}

insert(blink)