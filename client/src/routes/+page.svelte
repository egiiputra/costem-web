<script lang="ts">
	import { Fileupload, Label, Helper } from 'flowbite-svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	import Navbar from './Navbar.svelte';
	interface Scores {
		sehat: number;
		giberella: number;
		anthracnose: number;
	}

	interface Data {
		filename: string;
		scores: Scores | undefined;
		output: string | undefined;
	}

	let files: FileList | undefined = $state();

	let results: Data[] = $derived.by(() => {
		if (files == undefined) return [];

		let res = [];

		for (const file of files) {
			res.push({
				filename: file.name,
				scores: undefined,
				output: undefined
			});
		}
		return res;
	});

	$inspect(files);
	$inspect(results);

	function predicts() {
		fetch('localhost:8000/predicts', {
			method: 'POST',
			body: JSON.stringify({ username: 'example' }),
			headers: {
				'Content-Type': 'application/json'
			}
		});
	}
</script>

<Navbar />

<div class="mx-auto w-3/4">
	<Label for="with_helper" class="pb-2">Upload file</Label>
	<Fileupload id="with_helper" class="mb-2" accept="image/jpeg,image/png" bind:files multiple />
	<Helper>PNG or JPG; MAX: 2MB</Helper>

	<Table>
		<TableHead defaultRow={false}>
			<tr>
				<TableHeadCell rowspan="2">Thumbnail</TableHeadCell>
				<TableHeadCell rowspan="2">Filename</TableHeadCell>
				<TableHeadCell colspan="3">Scores</TableHeadCell>
				<TableHeadCell rowspan="2">Results</TableHeadCell>
			</tr>
			<tr>
				<TableHeadCell>sehat</TableHeadCell>
				<TableHeadCell>giberella</TableHeadCell>
				<TableHeadCell>anthracnose</TableHeadCell>
			</tr>
		</TableHead>
	<!--	<TableBody tableBodyClass="divide-y">
			<TableBodyRow>
				<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
				<TableBodyCell>Sliver</TableBodyCell>
				<TableBodyCell>Laptop</TableBodyCell>
				<TableBodyCell>$2999</TableBodyCell>
			</TableBodyRow>
			<TableBodyRow>
				<TableBodyCell>Microsoft Surface Pro</TableBodyCell>
				<TableBodyCell>White</TableBodyCell>
				<TableBodyCell>Laptop PC</TableBodyCell>
				<TableBodyCell>$1999</TableBodyCell>
			</TableBodyRow>
			<TableBodyRow>
				<TableBodyCell>Magic Mouse 2</TableBodyCell>
				<TableBodyCell>Black</TableBodyCell>
				<TableBodyCell>Accessories</TableBodyCell>
				<TableBodyCell>$99</TableBodyCell>
			</TableBodyRow>
		</TableBody>-->
	</Table>
</div>
