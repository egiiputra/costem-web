<script lang="ts">
    let files: FileList[] | [] = $state([]);

    function dropHandler(ev: DragEvent) {
        console.log("File(s) dropped");

        // Prevent default behavior (Prevent file from being opened)
        ev.preventDefault();

        console.log(ev.dataTransfer?.files);
        for (let i = 0; i < ev.dataTransfer?.files?.length ?? 0; i++) {
            files.push(ev.dataTransfer?.files.item(i));
        }
    }
    function dragOverHandler(ev: DragEvent) {
        console.log("File(s) in drop zone");

        // Prevent default behavior (Prevent file from being opened)
        ev.preventDefault();
    }
    $inspect(files);
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>

<div
    id="drop_zone"
    role="region"
    aria-labelledby="file-drop-label"
    ondrop={dropHandler}
    ondragover={dragOverHandler}>
    <p>Drag one or more files to this <i>drop zone</i>.</p>
</div>
<div>
    <ul>
        {#each files as file}
        <li>
            <span>{file.name}</span>
        </li>
        {/each}
    </ul>
</div>

<style>
    #drop_zone {
        border: 5px solid blue;
        width: 200px;
        height: 100px;
    }
</style>