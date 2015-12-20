<!DOCTYPE html>
<!--
This is a starter template page. Use this page to start your new project from
scratch. This page gets rid of all links and provides the needed markup only.
-->
<html class="app">

@include('partials.htmlheader')

<!--
BODY TAG OPTIONS:
=================
Apply one or more of the following classes to get the
desired effect
|---------------------------------------------------------|
| SKINS         | skin-blue                               |
|               | skin-black                              |
|               | skin-purple                             |
|               | skin-yellow                             |
|               | skin-red                                |
|               | skin-green                              |
|---------------------------------------------------------|
|LAYOUT OPTIONS | fixed                                   |
|               | layout-boxed                            |
|               | layout-top-nav                          |
|               | sidebar-collapse                        |
|               | sidebar-mini                            |
|---------------------------------------------------------|
-->
<body>
<section class="vbox">

    @include('partials.mainheader')


        <!-- Main content -->
        <section class="vbox ">
            <!-- Your Page Content Here -->
            @yield('main-content')
            <section style="display: block;height: 10%"></section>
        </section><!-- /.content -->



    @include('partials.scripts')

</section><!-- ./wrapper -->


</body>
</html>